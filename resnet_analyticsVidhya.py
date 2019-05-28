# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:23:21 2019

@author: BIG1KOR
"""

from imageai.Detection import ObjectDetection
import os
#%%
execution_path = os.getcwd()

data_path = os.path.join(execution_path, 'data')
model_path = os.path.join(execution_path, 'models')
#%%
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(model_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
#%%
custom_objects = detector.CustomObjects(person=True, car=False)
detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(data_path , "image.jpg"), output_image_path=os.path.join(execution_path , "image_new.png"), custom_objects=custom_objects, minimum_percentage_probability=65)
#%%
from IPython.display import Image
Image(os.path.join(data_path , "image.jpg"))