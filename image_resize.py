# pip install -U chitra

from chitra.image import Chitra
import matplotlib.pyplot as plt
import cv2

url = './CustomData/train/images/20201102_경기도_-_-_맑음_주간_실외_right_000004_0069936.png'
image = Chitra(url)

cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# [1.2733977e+03 3.9288733e+02 1.4136536e+03 5.0894998e+02 9.8771101e-01]
# img_path = './CustomData/train/images/20201102_경기도_-_-_맑음_주간_실외_right_000004_0069936.png'
# bbox = [1.2733977e+03, 3.9288733e+02, 1.4136536e+03, 5.0894998e+02, 9.8771101e-01]
# label = 'car'

# image = Chitra(img_path, bbox, label)

# # Chitra can rescale your bounding box automatically based on the new image size.
# image.resize_image_with_bbox((224, 224))

# print('rescaled bbox:', image.bounding_boxes)
# plt.imshow(image.draw_boxes())