#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PyQt5 import QtCore, QtGui, QtWidgets, uic

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


# In[ ]:




