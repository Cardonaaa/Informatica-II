#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# view.py
from PyQt5 import QtWidgets, uic, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()
        uic.loadUi('VentanaPrincipal.ui', self)
        self.controller = controller
        self.pushButton.clicked.connect(self.controller.open_ventana1)  
        self.pushButton_2.clicked.connect(self.controller.quit_application)

class Ventana1(QtWidgets.QMainWindow):
    def __init__(self, controller):
        super(Ventana1, self).__init__()
        uic.loadUi('Ventana1.ui', self)
        self.controller = controller
        self.pushButton.clicked.connect(self.controller.open_ventana2)  
        self.pushButton_2.clicked.connect(self.controller.open_ventana3)  
        self.pushButton_3.clicked.connect(self.controller.open_mainwindow)
    
    def on_pushButton_3_clicked(self):
        self.window = MainWindow(self.controller)
        self.window.show()
        self.hide()  # Oculta la ventana actual

class Ventana2(QtWidgets.QMainWindow):
    def __init__(self, controller):
        super(Ventana2, self).__init__()
        uic.loadUi('Ventana2.ui', self)
        self.controller = controller
        self.pushButton.clicked.connect(self.on_pushButton_clicked)  
        self.display_images()

    def display_images(self):
        images = self.controller.get_images('imagenes')
        for image in images:
            qimage = QtGui.QImage(image, image.shape[1], image.shape[0], image.strides[0], QtGui.QImage.Format_Grayscale8)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(qimage))

    def on_pushButton_clicked(self):
        self.window = Ventana1(self.controller)
        self.window.show()
        self.hide()  # Oculta la ventana actual

class Ventana3(QtWidgets.QMainWindow):
    def __init__(self, controller):
        super(Ventana3, self).__init__()
        uic.loadUi('Ventana3.ui', self)
        self.controller = controller
        self.pushButton.clicked.connect(self.on_pushButton_clicked)  
        self.pushButton_2.clicked.connect(self.controller.show_message)  

    def on_pushButton_clicked(self):
        self.window = Ventana1(self.controller)
        self.window.show()
        self.hide()  # Oculta la ventana actual

