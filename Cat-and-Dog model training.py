#Developing using Google Colab
#Uploading the Dataset as compressed folder as .zip or .tar to google Drive (Uploading as one zip file is faster than uploading thousands of small files as a folder)
from google.colab import drive
drive.mount('/content/drive')

# Change directory to where the compressed file is uploaded
import os
os.chdir('/content/drive/My Drive/Dataset/Kaggle/')

# Extract the file
!unzip dataset.zip

#Importing Libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt
import os

#Prepare Dataset
# Define paths for training and testing datasets
train_dir = './training_set/training_set/'
test_dir = './test_set/test_set/'

# Define image size and batch size
IMG_SIZE = (150, 150)
BATCH_SIZE = 32
