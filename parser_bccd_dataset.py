# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:37:44 2019

@author: BIG1KOR
"""
import pandas as pd
import os
import xml.etree.ElementTree as ET  

#%%
files = os.listdir('data\BCCD_Dataset\BCCD\Annotations')
file_names = [os.path.join('data\BCCD_Dataset\BCCD\Annotations', i) for i in files]
#%%
data_parsed = []

for item in file_names:
    tree = ET.parse(item)
    root = tree.getroot()    
    #parsing image name
    img_name = root.find('filename').text
    #parsing image items
    for object in root.findall('object'):
        cel_typ = object.find('name').text
        sizes = object.find('bndbox')
        xmin = sizes.find('xmin').text
        xmax = sizes.find('xmax').text
        ymin = sizes.find('ymin').text
        ymax = sizes.find('ymax').text
        data_parsed.append([img_name, cel_typ, xmin, xmax, ymin, ymax])
    

df_parsed = pd.DataFrame(data_parsed)
df_parsed.columns = ['image_names', 'cell_type', 'xmin', 'xmax', 'ymin', 'ymax']

df.head(5)