import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../DATA/00-puppy.jpg')
# plt.imshow(img)
# plt.show()

"""Convert from BGR to RGB"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

"""Convert from RGB to HSV"""
# img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# plt.imshow(img)
# plt.show()

"""Convert from RGB to HLS"""
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
plt.imshow(img)
plt.show()

