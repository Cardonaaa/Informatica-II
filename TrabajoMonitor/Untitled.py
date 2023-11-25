#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import sys
import pydicom
c
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QImage, QPixmap

class Modelo:
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

class VentanaEmergente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaEmergente, self).__init__()
        uic.loadUi('VentanaEmergente.ui', self)
        self.show()

class Vista(QtWidgets.QMainWindow):
    def __init__(self):
        super(Vista, self).__init__()
        uic.loadUi('MainWindow.ui', self)
        self.show()

class Controlador:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.modelo = Modelo()
        self.vista = Vista()
        self.ventana_emergente = None
        self.conectar_eventos()

    def conectar_eventos(self):
        self.vista.btnsesion.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        self.modelo.usuario = self.vista.textedit.text()
        self.modelo.contrasena = self.vista.textedit_2.text()
        print(f'Usuario: {self.modelo.usuario}, Contraseña: {self.modelo.contrasena}')
        self.ventana_emergente = VentanaEmergente()
        self.ventana_emergente.horizontalSlider.valueChanged.connect(self.cambiar_imagen)
        self.cambiar_imagen(0)

    def cambiar_imagen(self, value):
        self.modelo.indice_imagen = value % len(self.modelo.imagenes)
        imagen = self.modelo.imagenes[self.modelo.indice_imagen]
        # Convertir la matriz numpy a una imagen en escala de grises de 8 bits
        imagen = cv2.normalize(imagen, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        qimage = QImage(imagen.data, imagen.shape[1], imagen.shape[0], QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qimage)
        self.ventana_emergente.label.setPixmap(pixmap)

    def ejecutar(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar()


# In[ ]:




