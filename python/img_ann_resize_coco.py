# 참고 : https://stackoverflow.com/questions/49466033/resizing-image-and-its-bounding-box
# 치트라 참고 : https://chitra.readthedocs.io/en/latest/source/api/image/chitra-class/
import cv2
import numpy as np
import json
import os.path as osp
import os
from tqdm import tqdm
from PIL import Image

def drawBox(boxes, image):
    image = np.array(image)
    for i in range(0, len(boxes)):
        # changed color and width to make it visible
        cv2.rectangle(image, (boxes[0], boxes[1]), (boxes[0]+boxes[2], boxes[1]+boxes[3]),(255, 0, 0), 1)

    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def calc_resize_scale(w, h, target_w, target_h):
    x_scale = target_w / w
    y_scale = target_h / h

    return x_scale, y_scale

def image_resize_save(path, name, target_w, target_h):
    if not osp.isfile(osp.join(path, 'resize', 'images', name)):
        img = Image.open(osp.join(path, 'images', name))
        img_resize = img.resize((target_w, target_h), Image.LANCZOS)
        img_resize.save(osp.join(path, 'resize', 'images', name))

def bbox_resize(x_scale, y_scale, bbox):
    resize_x = int(np.round(bbox[0] * x_scale))
    resize_y = int(np.round(bbox[1] * y_scale))
    resize_width = int(np.round(bbox[2] * x_scale))
    resize_height = int(np.round(bbox[3] * y_scale))

    return [resize_x, resize_y, resize_width, resize_height]

if __name__ == "__main__":
    
    data_dir = './CustomData/train'
    input_json = './CustomData/train/label/Train.json'
    
    origin_w, origin_h = 1920, 1080
    target_w, target_h = 640, 480

    resize_json_data = {
        'images' : [], 'annotations': [], 'info': {}, 'licenses': [], 'categories': []
    }
    
    # 디렉토리 경로가 없다면 생성
    if not osp.isdir(osp.join(data_dir, 'resize', 'images')): 
        os.makedirs(osp.join(data_dir, 'resize', 'images')) 

    if not osp.isdir(osp.join(data_dir, 'resize', 'label')): 
        os.makedirs(osp.join(data_dir, 'resize', 'label')) 
    
    with open(input_json, encoding='utf-8') as json_reader:
        dataset = json.load(json_reader)
    
    x_scale, y_scale = calc_resize_scale(origin_w, origin_h, target_w, target_h)

    # info, licenses, categories 변동 없으므로 그대로 적용
    resize_json_data['info'] = dataset['info']
    resize_json_data['licenses'] = dataset['licenses']
    resize_json_data['categories'] = dataset['categories']

    for img_data in tqdm(dataset['images']):
        img_data['height'] = target_h
        img_data['width'] = target_w

        resize_json_data['images'].append(img_data)

        image_resize_save(osp.join(data_dir), img_data['file_name'], target_w, target_h)

    for ann_data in tqdm(dataset['annotations']):
        ann_data['bbox'] = bbox_resize(x_scale, y_scale, ann_data['bbox'])
        resize_json_data['annotations'].append(ann_data)


    with open(osp.join(data_dir, 'resize', 'label', 'Train_Resize.json'), 'w', encoding='utf-8') as f : 
	    json.dump(resize_json_data, f, indent=4, ensure_ascii=False)    
    

    # # 출력 확인 테스트
    # with open('./CustomData/train/resize/label/Train_Resize.json', encoding='utf-8') as json_reader:
    #      dataset = json.load(json_reader)

    # for ann_data in dataset['annotations']:
    #     if ann_data['image_id'] == 1:
    #         img = Image.open('./CustomData/train/resize/images/20201223_세종특별자치시_-_-_맑음_주간_실내_left_000089_0432081.png')
    #         bbox = ann_data['bbox']
    #         drawBox(bbox, img)




 

