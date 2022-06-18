from PIL import Image
import numpy as np
import albumentations

sample = Image.open("custom_data/images/20201102_경기도_-_-_맑음_주간_실외_right_000004_0069936.png")
sample_arr = np.asarray(sample)

print(sample_arr)



def resize_image(img_arr, bboxes, h, w):
    """
    :param img_arr: original image as a numpy array
    :param bboxes: bboxes as numpy array where each row is 'x_min', 'y_min', 'x_max', 'y_max', "class_id"
    :param h: resized height dimension of image
    :param w: resized weight dimension of image
    :return: dictionary containing {image:transformed, bboxes:['x_min', 'y_min', 'x_max', 'y_max', "class_id"]}
    """
    # create resize transform pipeline
    transform = albumentations.Compose(
        [albumentations.Resize(height=h, width=w, always_apply=True)],
        bbox_params=albumentations.BboxParams(format='pascal_voc'))

    transformed = transform(image=img_arr, bboxes=bboxes)

    return transformed


transformed_dict = resize_image(sample_arr, bboxes_og, 224, 224)

# contains the image as array
transformed_arr = transformed_dict["image"]

# contains the resized bounding boxes
transformed_info = np.array(list(map(list, transformed_dict["bboxes"]))).astype(float)