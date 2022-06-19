import json
import os, shutil
import random

# coco dataset train/val split
def split_dataset(input_json, output_dir, val_ratio, random_seed):
    random.seed(random_seed)

    with open(input_json, encoding='utf-8') as json_reader:
        dataset = json.load(json_reader)

    images = dataset['images']
    annotations = dataset['annotations']
    categories = dataset['categories']

    # file_name에 prefix 디렉토리까지 포함 (CocoDataset 클래스를 사용하는 경우)
    # for image in images:
    #     image['file_name'] = '{}/{}'.format(image['file_name'][0], image['file_name'])

    image_ids = [x.get('id') for x in images]
    image_ids.sort()
    random.shuffle(image_ids)

    num_val = int(len(image_ids) * val_ratio)
    num_train = len(image_ids) - num_val

    image_ids_val, image_ids_train = set(image_ids[:num_val]), set(image_ids[num_val:])

    train_images = [x for x in images if x.get('id') in image_ids_train]
    val_images = [x for x in images if x.get('id') in image_ids_val]
    train_annotations = [x for x in annotations if x.get('image_id') in image_ids_train]
    val_annotations = [x for x in annotations if x.get('image_id') in image_ids_val]

    train_data = {
        'images': train_images,
        'annotations': train_annotations,
        'categories': categories,
    }

    val_data = {
        'images': val_images,
        'annotations': val_annotations,
        'categories': categories,
    }

    #output_seed_dir = os.path.join(output_dir, f'seed{random_seed}')
    output_seed_dir = os.path.join(output_dir)
    os.makedirs(output_seed_dir, exist_ok=True)
<<<<<<< HEAD
    output_train_json = os.path.join(output_seed_dir, 'train_label.json')
    output_val_json = os.path.join(output_seed_dir, 'val_label.json')
=======
    output_train_json = os.path.join(output_seed_dir, 'train/train_label.json')
    output_val_json = os.path.join(output_seed_dir, 'val/val_label.json')
>>>>>>> 24522937184dc3109925fecd5ca3fecae2743f50

    # json 파일 한글로 작성하기 위해 encoding="utf-8", ensure_ascii=False 적용
    print(f'write {output_train_json}')
    with open(output_train_json, 'w', encoding="utf-8") as train_writer:
        json.dump(train_data, train_writer, ensure_ascii=False)

    print(f'write {output_val_json}')
    with open(output_val_json, 'w', encoding="utf-8") as val_writer:
        json.dump(val_data, val_writer, ensure_ascii=False)


def print_train_val_cnt(split_json_path):
<<<<<<< HEAD
    with open(os.path.join(split_json_path, 'train_label.json'), encoding='utf-8') as fh:
=======
    with open(os.path.join(split_json_path + 'train_label.json'), encoding='utf-8') as fh:
>>>>>>> 24522937184dc3109925fecd5ca3fecae2743f50
        train_data = json.load(fh)

    print('-'*50)
    print('training data')
    print(f'images: {len(train_data["images"])}')
    print(f'annotations: {len(train_data["annotations"])}')
    print(f'categories: {len(train_data["categories"])}')

    # split validation data check
<<<<<<< HEAD
    with open(os.path.join(split_json_path, 'val_label.json'), encoding='utf-8') as fh:
=======
    with open(os.path.join(split_json_path + 'val_label.json'), encoding='utf-8') as fh:
>>>>>>> 24522937184dc3109925fecd5ca3fecae2743f50
        val_data = json.load(fh)

    print('-'*50)
    print('validation data')
    print(f'images: {len(val_data["images"])}')
    print(f'annotations: {len(val_data["annotations"])}')
    print(f'categories: {len(val_data["categories"])}')

if __name__ == "__main__":
    src_data_root = "./CustomData"
    dest_data_root = "./Split_CustomData"

<<<<<<< HEAD
    # 폴더 없을 시, 생성
    # train
    if not os.path.isdir(os.path.join(dest_data_root, "train_img")):
        os.mkdir(os.path.join(dest_data_root, "train_img"))
    
        # validation
    if not os.path.isdir(os.path.join(dest_data_root, "val_img")):
        os.mkdir(os.path.join(dest_data_root, "val_img"))

=======
>>>>>>> 24522937184dc3109925fecd5ca3fecae2743f50
    split_dataset(input_json=os.path.join(src_data_root, "train/label/Train.json"),
                output_dir=dest_data_root,
                val_ratio=0.2,
                random_seed=13)

    print_train_val_cnt(dest_data_root)
    
    with open(os.path.join(os.path.join(dest_data_root, 'train_label.json')), encoding='utf-8') as fh:
        split_train_data_list = json.load(fh)
    
    with open(os.path.join(os.path.join(dest_data_root, 'val_label.json')), encoding='utf-8') as fh:
        split_val_data_list = json.load(fh)
    
<<<<<<< HEAD
=======
    # 폴더 없을 시, 생성
    # train
    if not os.path.isdir(os.path.join(dest_data_root, "train_img")):
        os.mkdir(os.path.join(dest_data_root, "train_img"))
    
>>>>>>> 24522937184dc3109925fecd5ca3fecae2743f50
    for i in split_train_data_list['images']:
        try:
            shutil.move(os.path.join(src_data_root, "train/images/"+i['file_name']), os.path.join(dest_data_root, "train_img/"+i['file_name']))
        except:
            pass

<<<<<<< HEAD
=======
    # validation
    if not os.path.isdir(os.path.join(dest_data_root, "val_img")):
        os.mkdir(os.path.join(dest_data_root, "val_img"))

>>>>>>> 24522937184dc3109925fecd5ca3fecae2743f50
    for i in split_val_data_list['images']:
        try:
            shutil.move(os.path.join(src_data_root, "train/images/"+i['file_name']), os.path.join(dest_data_root, "val_img/"+i['file_name']))
        except:
            pass



