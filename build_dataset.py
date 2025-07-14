import shutil
from main import config # from main file 
from imutils import paths
import random
import shutil
import os

# grab the paths to all input images in the original input directory
# and shuffle them
image_paths = list(paths.list_images(config.original_input_dataset))
random.seed(42)
random.shuffle(image_paths)
print(image_paths) # list of image paths i.e. ['malaria/cell_images/Para...', ...]

# compute the training and testing split
i = int(len(image_paths) * config.val_split)
print(i)
trainPaths = image_paths[:i]
valPaths = image_paths[i:]