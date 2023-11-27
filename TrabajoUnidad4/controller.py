#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# controller.py
from PyQt5 import QtWidgets
from model import Model
from view import MainWindow, Ventana1, Ventana2, Ventana3

class Controller:
    def __init__(self):
        self.model = Model()
        self.mainwindow = MainWindow(self)
        self.ventana1 = Ventana1(self)
        self.ventana2 = Ventana2(self)
        self.ventana3 = Ventana3(self)

    def start(self):
        self.mainwindow.show()

    def open_mainwindow(self):
        self.mainwindow.show()

    def open_ventana1(self):
        self.ventana1.show()

    def open_ventana2(self):
        self.ventana2.show()

    def open_ventana3(self):
        self.ventana3.show()

    def quit_application(self):
        QtWidgets.QApplication.quit()

    def get_images(self, image_folder):
        return self.model.get_images(image_folder)

    def show_message(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Respuesta")
        msg.setText("La respuesta correcta es '206 huesos'")
        msg.exec_()

