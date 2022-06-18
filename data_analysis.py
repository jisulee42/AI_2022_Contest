from __future__ import annotations
import glob
import json
import os
from collections import defaultdict
import pandas as pd
import csv
'''
# JSON Format
images : file_name, license, coco_url, height, width, data_captured, flickr_url, id
annotations : bbox, segmentation, iscrowd, area, image_id, category_id, id
info : description, url, version, year, contributor, created
licenses : url, id, name
categories : supercategory, name, id
'''

img_dict = defaultdict(list)
path = 'custom_data\label\Train.json'

# 전체 json data 읽기
with open(path, "r", encoding="utf-8") as f:
    json_data = json.load(f)

# images
for data in json_data['images']:
    img_dict['id'].append(data['id'])
    img_dict['file_name'].append(data['file_name'])
    img_dict['height'].append(data['height'])
    img_dict['width'].append(data['width'])

df = pd.DataFrame(img_dict, index=False)
df.to_csv("custom_data/images.csv")

anno_dict = defaultdict(list)

for data in json_data['annotations']:
    anno_dict['id'].append(data['id'])
    anno_dict['bbox'].append(data['bbox'])
    anno_dict['area'].append(data['area'])
    anno_dict['image_id'].append(data['image_id'])
    anno_dict['category_id'].append(data['category_id'])

df = pd.DataFrame(anno_dict, index=False)
df.to_csv("custom_data/annotations.csv")

# print(list(csv_dict.keys()))
# csv_file = "custom_data.csv"
# csv_columns = ['file_name', 'height', 'width', 'id']

# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in csv_dict:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")

