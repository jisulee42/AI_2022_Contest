import argparse
from mmdet.apis import init_detector, inference_detector
from mmdet.apis import show_result_pyplot
from tqdm import tqdm
import os.path as osp
import mmcv
import json
import numpy as np

# model.cfg = cfg
# result = inference_detector(model, img)
# show_result_pyplot(model, img, result, 0.75)
# # 인자값을 받을 수 있는 인스턴스 생성
# parser = argparse.ArgumentParser(description='사용법 테스트입니다.')

# # 입력받을 인자값 등록
# parser.add_argument('--target', required=True, help='어느 것을 요구하냐')
# parser.add_argument('--env', required=False, default='dev', help='실행환경은 뭐냐')

# # 입력받은 인자값을 args에 저장 (type: namespace)
# args = parser.parse_args()

# # 입력받은 인자값 출력
# print(args.target)
# print(args.env)
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            # 👇️ alternatively use str()
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def submission(model, data):
    img_path = osp.join(test_dir, 'images', data['file_name'])
    img = mmcv.imread(img_path)
    results = inference_detector(model, img)
    
    for result in results:
        cnt = 0
        for r in result:
            cnt += 1
            if r[4] >= 0.75 :
                sub_dir = {}
                sub_dir['image_id'] = data['id']
                sub_dir['category_id'] = cnt
                sub_dir['bbox'] = [r[0],r[1], r[2]-r[0], r[3]-r[1]]
                sub_dir['score'] = r[4]
                sub_dir['segmentation'] = []
                submission_list.append(sub_dir)

    #sub_dir['image_id'] = data['id']

if __name__ == "__main__":
    submission_list = []

    MMDET_CONFIG = './mmdetection/configs/custom_config.py'
    MMDET_CHECKPOINT = './work_dir/faster_rcnn_epoch1_2022620_205249.ptn'
    test_dir = './CustomData/test'

    model = init_detector(MMDET_CONFIG, MMDET_CHECKPOINT, device='cuda:0')
    #test_json_path = './CustomData/test/Test_Images_Information.json'

    with open(osp.join(test_dir, 'Test_Images_Information.json'), encoding='utf-8') as json_reader:
        dataset = json.load(json_reader)
    
    #count = 0
    for img_data in tqdm(dataset['images']):
        submission(model, img_data)
        # count += 1
        # if count == 100:
        #     break

    with open('./submission.json', 'w', encoding='utf-8') as f : 
	    json.dump(submission_list, f, ensure_ascii=False, cls=NpEncoder)   

    

    

