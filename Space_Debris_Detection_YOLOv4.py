# -*- coding: utf-8 -*-
"""Research_Paper_Space_Debris_Detection_v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a_cJryVrHDibekQLUA46EMlG-ZO3UpXJ

# **Mounting the drive and importing the neccesary packages**
"""

# Mount the google drive
from google.colab import drive
drive.mount('/content/drive')

# Import necessary packages
import os
import shutil

"""# **Setting the path of the folder which is used for building the object detection model**"""

path = '/content/drive/My Drive/Research_Project_V1'
os.chdir(path)

"""# **Cloned the Darknet repository for building the custom model, updated parameters manually in "Makefile" file and verified the installation of the Darknet folder**"""

# Clone DarkNet Repo
!git clone https://github.com/AlexeyAB/darknet

# verify CUDA version
! /usr/local/cuda/bin/nvcc --version

# Compile DarkNet Framework in order to use related files for training Object Detection Model
os.chdir('/content/drive/My Drive/Research_Project_V1/darknet')
!sudo chmod +x darknet
!make

# Verify installation
!sudo chmod +x darknet
!./darknet

"""# **Created a symbolic link to shorten the drive path and moved the images folder to the model building folder**"""

# Create symbolic link
!ln -s '/content/drive/My Drive' /driveV1

shutil.move("/driveV1/space_data", "/driveV1/Research_Project_V1/darknet/data/")

"""# **Setting image folder path to create training and testing files for model building, also created "backup" folder to store the weights ***"""

# Setting image directory path
img_path = '/driveV1/Research_Project_V1/darknet/data/space_data'
os.chdir(img_path)

#Iterate through each image found in the directory and save the corresponding path to the list called as path_list

path_list = []

# Go through all the image files in the directory
for current_dir, dirs, files in os.walk('.'):
  # Iterating through all the files
  for f in files:
    # Check if the file extension ends with '.jpg'
    if f.endswith('.jpg'):
      # Prepare file path to save into train.txt
      file_loc = img_path + '/' + f
      # Append the path data into list "path_list". New line character \n is used to write the new content
      path_list.append(file_loc + '\n')

# Divide the data into 80:20 ratio. get 20% of data from path_list to write into the test.txt file
path_list_test = path_list[:int(len(path_list) * 0.20)]

# Delete the same 20% records from the path_list as that 20% data is in the path_list_test now
path_list = path_list[int(len(path_list) * 0.20):]

# Create train.txt file and write 80% of data (lines) inside it.
with open('train.txt', 'w') as train:
  # Iterate through all the elements in the list
  for i in path_list:
    # Write the current path at the end of the file
    train.write(i)

# Create test.txt file and write 20% of data (lines) inside it.
with open('test.txt', 'w') as test:
  # Iterate through all the elements in the list
  for i in path_list_test:
    # Write the current path at the end of the file
    test.write(i)

# Initialize the counter
i = 0

# Create classes.names files by reading from existing classes.txt file
with open(img_path + '/' + 'classes.names', 'w') as cls, \
     open(img_path + '/' + 'classes.txt', 'r') as text:

     # Iterate through individual lines in classes.txt file and wrte them into classes.names file
     for l in text:
       cls.write(l)

       # Increasing counter
       i += 1

# create image_data.data
with open(img_path + '/' + 'image_data.data', 'w') as data:
  #write number of classes
  data.write('classes = ' + str(i) + '\n')

  #write fully qualified path of the train.txt file
  data.write('train = ' + img_path + '/' + 'train.txt' + '\n')

  #write fully qualified path of the test.txt file
  data.write('valid = ' + img_path + '/' + 'test.txt' + '\n')

  #write fully qualified path of the classes.names file
  data.write('names = ' + img_path + '/' + 'classes.names' + '\n')

  #specify folder path to save trained model weights
  data.write('backup = backup')

# Change the directory path and provide permission to the darknet folder
os.chdir('/driveV1/Research_Project_V1/darknet')
!sudo chmod +x darknet
!./darknet

"""# **Downloaded convolution file for training custom model for object detection**"""

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4.conv.137

"""# **Executed the convolution file**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg yolov4.conv.137 -dont_show -map

!sudo chmod +x darknet
!./darknet

"""# **Custom configuration file got interrupted while execution (1st time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (2nd time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (3rd time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (4th time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (5th time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (6th time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (7th time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Custom configuration file got interrupted while execution (8th time), so using the last weights stored in the back up file to restore the execution and train the model again**"""

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights -dont_show

"""# **Checking the Mean Average Precision (mAP) for 1000 iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_1000.weights

"""# **Checking the Mean Average Precision (mAP) for 2000 iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_2000.weights

"""# **Checking the Mean Average Precision (mAP) for 3000 iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_3000.weights

"""# **Checking the Mean Average Precision (mAP) for 4000 weights iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_4000.weights

"""# **Checking the Mean Average Precision (mAP) for 5000 weights iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_5000.weights

"""# **Checking the Mean Average Precision (mAP) for 6000 weights iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_6000.weights

"""# **Checking the Mean Average Precision (mAP) for final weights iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_final.weights

"""# **Checking the Mean Average Precision (mAP) for last weights iterations**"""

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_last.weights

"""# **Testing image using last weights as it showed the maximum mAP**"""

!./darknet detector test data/space_data/image_data.data cfg/yolov4-obj.cfg /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_6000.weights data/deb1.jpg -thresh 0.3 -ext_output -dont_show

"""# **Displaying the output image with bounding boxes and labels using OpenCV**"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

image = cv2.imread('predictions.jpg')
fig = plt.gcf()
fig.set_size_inches(12, 14)
plt.imshow(image)

"""# **Saving the output image**"""

from google.colab import files
files.download('predictions.jpg')

"""# **Testing video using last weights as it showed the maximum mAP**"""

!./darknet detector demo data/space_data/image_data.data cfg/yolov4-obj.cfg -dont_show /driveV1/Research_Project_V1/darknet/backup/yolov4-obj_2000.weights data/space_debris2.mp4 -i 0 -out_filename obj_det_video.avi -ext_output -dont_show

"""# **Saving the output video**"""

from google.colab import files
files.download('obj_det_video.avi')

"""# **Testing other video (2)**"""

!./darknet detector demo data/space_data/image_data.data cfg/yolov4-obj.cfg -dont_show /Newdrive/Research_Project2/darknet/backup/yolov4-obj_last.weights data/satellite1.mp4 -i 0 -out_filename obj_det_video.avi -ext_output

"""# **Saving the video**"""

from google.colab import files
files.download('obj_det_video.avi')

"""# **Testing another video**"""

!./darknet detector demo data/space_data/image_data.data cfg/yolov4-obj.cfg -dont_show /Newdrive/Research_Project2/darknet/backup/yolov4-obj_last.weights data/satellite2.mp4 -i 0 -out_filename obj_det_video.avi -ext_output

"""# **Saving the video**"""

from google.colab import files
files.download('obj_det_video.avi')

!./darknet detector train data/space_data/image_data.data cfg/yolov4-obj.cfg /Newdrive/Research_Project2/darknet/backup/yolov4-obj_last.weights -dont_show

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /Newdrive/Research_Project2/darknet/backup/yolov4-obj_4000.weights

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /Newdrive/Research_Project2/darknet/backup/yolov4-obj_5000.weights

!./darknet detector map data/space_data/image_data.data cfg/yolov4-obj.cfg /Newdrive/Research_Project2/darknet/backup/yolov4-obj_last.weights

!./darknet detector test data/space_data/image_data.data cfg/yolov4-obj.cfg /Newdrive/Research_Project2/darknet/backup/yolov4-obj_3000.weights data/deb1.jpg -thresh 0.3 -ext_output

# Commented out IPython magic to ensure Python compatibility.
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

image = cv2.imread('predictions.jpg')
fig = plt.gcf()
fig.set_size_inches(12, 14)
plt.imshow(image)

from google.colab import files
files.download('predictions.jpg')

!./darknet detector demo data/space_data/image_data.data cfg/yolov4-obj.cfg -dont_show /Newdrive/Research_Project2/darknet/backup/yolov4-obj_3000.weights data/satellite2.mp4 -i 0 -out_filename obj_det_video.avi -ext_output

from google.colab import files
files.download('obj_det_video.avi')

!./darknet detector demo data/space_data/image_data.data cfg/yolov4-obj.cfg -dont_show /Newdrive/Research_Project2/darknet/backup/yolov4-obj_last.weights data/satellite2.mp4 -i 0 -out_filename obj_det_video.avi -ext_output

from google.colab import files
files.download('obj_det_video.avi')