import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread("drive/MyDrive/imagensColab/boat.tif")
plt.imshow(imagem)

def non_local_means(image, h, window_size, patch_size):
    filtered_image = np.zeros_like(image)
    padded_image = np.pad(image, patch_size // 2, mode='reflect')
    height, width = image.shape

    for y in range(height):
        for x in range(width):
            patch_center = (y + patch_size // 2, x + patch_size // 2)
            search_window = padded_image[
                patch_center[0] - window_size // 2:patch_center[0] + window_size // 2 + 1,
                patch_center[1] - window_size // 2:patch_center[1] + window_size // 2 + 1
            ]
            
            distances = np.sum((search_window - search_window[patch_size // 2, patch_size // 2])**2, axis=2)
            weights = np.exp(-distances / h)
            
            patch = padded_image[
                patch_center[0] - patch_size // 2:patch_center[0] + patch_size // 2 + 1,
                patch_center[1] - patch_size // 2:patch_center[1] + patch_size // 2 + 1
            ]
            
            weighted_patch = patch * np.expand_dims(weights, axis=2)
            filtered_value = np.sum(weighted_patch) / np.sum(weights)
            filtered_image[y, x] = filtered_value
    
    return filtered_image

