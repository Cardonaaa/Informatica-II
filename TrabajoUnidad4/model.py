#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# model.py
from pydicom import dcmread
import numpy as np
import cv2
import glob

class Model:
    def get_images(self, image_folder):
        images = []
        for filename in glob.glob(image_folder + '/*.dcm'):
            ds = dcmread(filename)
            image = np.array(ds.pixel_array)
            image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            images.append(image)
        return images

