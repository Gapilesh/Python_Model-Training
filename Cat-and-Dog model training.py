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

# Create data generators with augmentation
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, zoom_range=0.15, width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

# Load training and testing datasets
train_generator = train_datagen.flow_from_directory(train_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='binary')
test_generator = test_datagen.flow_from_directory(test_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='binary')

#Build CNN Model
