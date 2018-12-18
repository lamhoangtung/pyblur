import numpy as np
from PIL import ImageFilter

# gaussianbandwidths = [1, 1.5, 2] #, 2, 2.5, 3, 3.5]
gaussianbandwidths = np.random.choice([1, 1.5, 2], 1, p=[0.5, 0.3, 0.2])[0]


def GaussianBlur_random(img):
    return GaussianBlur(img, np.random.choice([1, 1.5, 2], 1, p=[0.5, 0.3, 0.2])[0])


def GaussianBlur(img, bandwidth):
    img = img.filter(ImageFilter.GaussianBlur(bandwidth))
    return img
