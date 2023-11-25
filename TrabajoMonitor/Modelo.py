#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pydicom
import cv2
import numpy as np

class User:
    def __init__(self):
        self.usuario = ""
        self.contrasena = ""
        self.imagenes = []
        self.indice_imagen = 0

        # Leer los archivos .dcm
        for filename in os.listdir('imagenes'):
            if filename.endswith('.dcm'):
                ds = pydicom.dcmread(os.path.join('imagenes', filename))
                self.imagenes.append(ds.pixel_array)


# In[ ]:




