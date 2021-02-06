# import the necessary packages
import os

# initialize the base path for the front/rear vehicle dataset
BASE_PATH = "dlib_front_and_rear_vehicles_v1"

# build the path to the input training and testing XML files
TRAIN_XML = 'E:/PROGRAMMING_DOCUMENTS/computer_vision/vision_2020/IB_Code/chapter17-training_ssd/dlib_front_and_rear_vehicles_v1/training.xml'
''
TEST_XML = 'E:/PROGRAMMING_DOCUMENTS/computer_vision/vision_2020/IB_Code/chapter17-training_ssd/dlib_front_and_rear_vehicles_v1/testing.xml'

# build the path to the output training and testing record files,
# along with the class labels file
TRAIN_RECORD = 'E:/PROGRAMMING_DOCUMENTS/computer_vision/vision_2020/IB_Code/chapter17-training_ssd/dlib_front_and_rear_vehicles_v1/records/training.record'

TEST_RECORD = 'E:/PROGRAMMING_DOCUMENTS/computer_vision/vision_2020/IB_Code/chapter17-training_ssd/dlib_front_and_rear_vehicles_v1/records/testing.record'
CLASSES_FILE = 'E:/PROGRAMMING_DOCUMENTS/computer_vision/vision_2020/IB_Code/chapter17-training_ssd/dlib_front_and_rear_vehicles_v1/records/classes.pbtxt'

# initialize the class labels dictionary
CLASSES = {"rear": 1, "front": 2}
