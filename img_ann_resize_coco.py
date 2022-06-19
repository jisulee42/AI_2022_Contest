# 참고 : https://stackoverflow.com/questions/49466033/resizing-image-and-its-bounding-box
# 치트라 참고 : https://chitra.readthedocs.io/en/latest/source/api/image/chitra-class/
from __future__ import annotations
import cv2
import numpy as np
import json
import os.path as osp
from chitra.image import Chitra
import matplotlib.pyplot as plt
from regex import I

# def drawBox(boxes, image):
#     for i in range(0, len(boxes)):
#         # changed color and width to make it visible
#         cv2.rectangle(image, (boxes[i][2], boxes[i][3]), (boxes[i][4], boxes[i][5]), (255, 0, 0), 1)
#     cv2.imshow("img", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# def resize(img_name, target_w, target_h, x, y, w, h):
#     # imageToPredict = cv2.imread("img.jpg", 3)
#     imageToPredict = cv2.imread(osp.join("./CustomData/test/images", img_name), 3)
#     print(imageToPredict.shape)

#     # Note: flipped comparing to your original code!
#     # x_ = imageToPredict.shape[0]
#     # y_ = imageToPredict.shape[1]
#     y_ = imageToPredict.shape[0]
#     x_ = imageToPredict.shape[1]

#     targetSize = 416
#     x_scale = targetSize / x_
#     y_scale = targetSize / y_
#     print(x_scale, y_scale)
#     img = cv2.resize(imageToPredict, (targetSize, targetSize));
#     print(img.shape)
#     img = np.array(img);

#     # original frame as named values
#     #(origLeft, origTop, origRight, origBottom) = (160, 35, 555, 470)
#     (origLeft, origTop, origRight, origBottom) = (1.8201077e+03, 5.3748688e+02, 1.9181411e+03, 7.6707251e+02)

#     x = int(np.round(origLeft * x_scale))
#     y = int(np.round(origTop * y_scale))
#     xmax = int(np.round(origRight * x_scale))
#     ymax = int(np.round(origBottom * y_scale))
#     # Box.drawBox([[1, 0, x, y, xmax, ymax]], img)
#     drawBox([[1, 0, x, y, xmax, ymax]], img)
def resize_image_save(image, path):
    pass

def bbox_resize(img_dir, file_name, bbox, label, resize_wh):
    path = osp.join(img_dir, file_name)
    tmp_bbox = [[bbox[0], bbox[1], bbox[0]+bbox[2], bbox[1]+bbox[3]]]
    image = Chitra(path, tmp_bbox, label)
    image.resize_image_with_bbox(resize_wh)
    

    return [image.bboxes.bboxes[0].x1_int, image.bboxes.bboxes[0].y1_int, int(image.bboxes.bboxes[0].width), int(image.bboxes.bboxes[0].height)]

if __name__ == "__main__":
    #cvTest()
    img_dir = './CustomData/train/images'
    input_json = './CustomData/train/label/Train.json'
    resize_w, resize_h = 640, 480

    resize_json_data = {
        'images' : [], 'annotations': [], 'info': {}, 'licenses': [], 'categories': []
    }

    with open(input_json, encoding='utf-8') as json_reader:
        dataset = json.load(json_reader)
        
    # info, licenses, categories 변동 없으므로 그대로 적용
    resize_json_data['info'] = dataset['info']
    resize_json_data['licenses'] = dataset['licenses']
    resize_json_data['categories'] = dataset['categories']

    for img_data in dataset['images']:
        img_data['height'] = resize_h
        img_data['width'] = resize_w

        resize_json_data['images'].append(img_data)

        for ann_data in dataset['annotations']:
            if img_data['id'] == ann_data['image_id']:
                print(ann_data['bbox'])
                print(bbox_resize(img_dir, img_data['file_name'], ann_data['bbox'], ann_data['category_id'], (resize_w, resize_h)))
                print('-'*50)
        

    #print(resize_json_data)

    # img_list =  []
    # for img_data in dataset['images']:
    #     pass
    #     #print(data['id'])
    # for ann_data in dataset['annotations']:
    #     print(ann_data)




 

