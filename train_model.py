# set the mpl backend so figures can be saved in background
import matplotlib
matplotlib.use("Agg")

# import the necessary packages
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator # for data augmentation
from tensorflow.keras.callbacks import LearningRateScheduler # for learning rate scheduler
from tensorflow.keras.optimizers import SGD # stochastic gradient descent
from tensorflow.keras.utils import to_categorical # for one-hot encoding
from main.resnet import ResNet # for the ResNet model
from main import config # for the configuration
from sklearn.metrics import classification_report # for the classification report
from imutils import paths # for the paths
import matplotlib.pyplot as plt # for the plot
import numpy as np # for the numpy
import argparse # for the argument parser

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output loss/accuracy plot")
args = vars(ap.parse_args())