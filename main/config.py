# store all constant vawriables
import os

# initialize the path to the *original* input directory of images
original_input_dataset =  "malaria/cell_images"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
base_path = "malaria"

# derive the training, validation, and testing directories
# (where the dataset will be built during building)
train_path = os.path.sep.join([base_path, "training"])
val_path = os.path.sep.join([base_path, "validation"])
test_path = os.path.sep.join([base_path, "testing"])

# define the proportion of data that will be used for training
train_split = 0.8

# the proportion of validation data
val_split = 0.1