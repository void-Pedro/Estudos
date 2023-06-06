import numpy as np
from glob import glob
from PIL import Image
from matplotlib import pyplot as plt
from felzenszwalb_segmentation import segment
image_files = glob('/users/ADM/desktop/imagens/*')
image = np.array(Image.open(image_files[3]))
segmented_image = segment(image, 0.2, 400, 50)
fig = plt.figure(figsize=(12,12))
a = fig.add_subplot(1, 2, 1)
plt.imshow(image)
a = fig.add_subplot(1, 2, 2)
plt.imshow(segmented_image.astype(np.uint8))
plt.show()