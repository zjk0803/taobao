import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib as mpl

digits = datasets.load_digits()
print(digits.data.shape)
print(digits.images.shape)
img = digits.images[1,:,:]
plt.imshow(img,cmap='gray')
plt.show()
for image_index in range(10):
    subplot_index = image_index + 1
    plt.subplot(2,5,subplot_index)
    plt.imshow(digits.images[image_index,:,:],cmap='gray')
    plt.show()