from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Modelo:
    def __init__(self):
        self.usuario = ""
        self.contrasena = ""

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
        self.conectar_eventos()

    def conectar_eventos(self):
        self.vista.btnsesion.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        self.modelo.usuario = self.vista.textedit.text()
        self.modelo.contrasena = self.vista.textedit_2.text()
        print(f'Usuario: {self.modelo.usuario}, Contraseña: {self.modelo.contrasena}')

    def ejecutar(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar()
