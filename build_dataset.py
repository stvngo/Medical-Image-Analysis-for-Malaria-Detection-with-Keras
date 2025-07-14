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
# list of image paths i.e. ['malaria/cell_images/Para...', ...]

# compute the training and testing split
i = int(len(image_paths) * config.train_split)
print(i)
trainPaths = image_paths[:i] # 80%
testPaths = image_paths[i:] # 20%

# using part of the training data for validation
i = int(len(trainPaths) * config.val_split)
valPaths = trainPaths[:i] # 10% of trainPaths
trainPaths = trainPaths[i:] # 90% of trainPaths

# name of split, paths for split, path to output dir for split
datasets = [("training", trainPaths, config.train_path), 
            ("validation", valPaths, config.val_path), 
            ("testing", testPaths, config.test_path)]

# loop through datasets
for (dType, imagePaths, baseOutput) in datasets:
    # show which data split we are creating
    print(f"[INFO] building '{dType}' split")

    # if output base directory DNE, create it
    if not os.path.exists(baseOutput):
        print(f"[INFO] 'creating {baseOutput}' directory")
        os.makedirs(baseOutput)

    for inputPath in imagePaths:
        # extract the filename of the input image along with its
        # corresponding label (os.path.sep == '/' for macOS)
        filename = inputPath.split(os.path.sep)[-1]
        label = inputPath.split(os.path.sep)[-2] 
        # parasitized or uninfected
        
        filename = os.path.basename(inputPath)

        # build the path to the label subdirectory
        labelPath = os.path.sep.join([baseOutput, label])
        # i.e C4251.../Parasitized or C1234/Uninfected

        # if label output directory does not exist, create it
        if not os.path.exists(labelPath):
            print(f"[INFO] 'creating {labelPath}' directory")
            os.makedirs(labelPath)

        # construct the path to the destination image and then copy
        # the image itself into the subdirectory
        p = os.path.sep.join([labelPath, filename])
        shutil.copy2(inputPath, p)

