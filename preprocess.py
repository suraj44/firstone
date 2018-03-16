import os

# For restoring pickled data
import pickle

# Suffle data set
import random

import numpy as np
import os

import shutil

# Directory containing extracted CROHME data
data_dir = 'data'


classes = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '(', ')', '[', ']', '+', '-', '/', '=', 'geq', 'gt', 'leq', 'lt', '\\neq', '\\times', '\div']
num_classes = len(classes)




data_path = '/home/surajnitk4/HES/extracted_images/'
train_path = '/home/surajnitk4/HES/train/'
valid_path = '/home/surajnitk4/HES/valid/'



for folder in os.scandir(data_path):
	if (len(str(folder.name))==1 and((97<=ord(str(folder.name))<=122) or (65<=ord(str(folder.name))<=90))) or (folder.name in classes):
		i = 0
		if not os.path.exists(train_path + str(folder.name)):
			os.makedirs(train_path + str(folder.name))
		if not os.path.exists(valid_path + str(folder.name)):
			os.makedirs(valid_path + str(folder.name))
		for file in os.listdir(os.path.join(data_path,str(folder.name))):
			i = i+1
			i = i%10
			if i<8:
				shutil.move((data_path + str(folder.name)  + '/' +  str(file)),(train_path + str(folder.name) + '/' ))

			else:
				shutil.move((data_path + str(folder.name)  + '/' +  str(file)),(valid_path + str(folder.name) + '/' ))

	#classes.remove(str(folder.name))




