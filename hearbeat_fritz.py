# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:35:40 2019

@author: BIG1KOR
"""
from imageai.Detection import VideoObjectDetection
#%%
import os
import cv2
#%%
execution_path = os.path.join(os.getcwd())
#%%

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "models\\yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "data\\traffic-mini.mp4"),
                                output_file_path=os.path.join(execution_path, "traffic_mini_detected_1")
                                , frames_per_second=29, log_progress=True)
print(video_path)
#%%