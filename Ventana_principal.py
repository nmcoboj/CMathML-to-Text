# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from module import TexToES
import imagen
from win32com.client import Dispatch


texto_final = ''

class CMathML2Txt(object):

    def __init__(self):
        self.msg = 'Inicio del proceso'  # Inicializa impresión (1)
        self.input = ''                  # Inicializa entrada
        self.output = ''                 # Inicializa salida

    def runcmath2txt(self,idioma):

        """
        :param input: Representación en cadena de una expresión matemática en CMathMl

        """
        print(self.msg)  # Imprime inicializacion anterior (1)
        a = TexToES(latex=None, cmathml=self.input, verbose=False, filename=None)  # Guarda función de otro programa en una variable
        self.output = a.process_input(idioma)
        print("Proceso Finalizado")
        print("salida=" + self.output)
        global texto_final
        texto_final = self.output
        print(texto_final)
        f = open('Texto.txt', 'w')
        f.write(texto_final)
        f.close()

    def read_file_Mathml(self, filename):
        """
        Leer el archivo que contiene el código de la fórmula en CMathML

        """
        self.__input_logging("Archivo", filename)
        aux = ''
        with open(filename, 'r+') as f:
            for line in f.readlines():
                aux = aux + line.rstrip('\n')
        self.input = aux
        print(aux)

    def __input_logging(self, msg, input):
        print("++++++++++ Procesando %s ++++++++++" % msg)
        print("%s recibido:\n%s\n" % (msg, input))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Boton = QtWidgets.QPushButton(self.centralwidget)
        self.Boton.setGeometry(QtCore.QRect(290, 20, 111, 41))
        self.Boton.setObjectName("Boton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 270, 51, 16))
        self.label.setObjectName("label")
        self.Texto = QtWidgets.QLabel(self.centralwidget)
        self.Texto.setGeometry(QtCore.QRect(160, 270, 441, 16))
        self.Texto.setObjectName("Texto")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 310, 55, 16))
        self.label_3.setObjectName("label_3")
        self.Reproducir = QtWidgets.QPushButton(self.centralwidget)
        self.Reproducir.setGeometry(QtCore.QRect(160, 300, 93, 41))
        self.Reproducir.setObjectName("Reproducir")
        self.Imagen = QtWidgets.QLabel(self.centralwidget)
        self.Imagen.setGeometry(QtCore.QRect(240, 150, 200, 100))
        self.Imagen.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Imagen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Imagen.setText("")
        self.Imagen.setScaledContents(True)
        self.Imagen.setObjectName("Imagen")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 31, 51, 21))
        self.label_2.setObjectName("label_2")
        self.comboIdioma = QtWidgets.QComboBox(self.centralwidget)
        self.comboIdioma.setGeometry(QtCore.QRect(80, 30, 85, 21))
        self.comboIdioma.setObjectName("comboIdioma")
        self.comboIdioma.addItem("")
        self.comboIdioma.addItem("")
        self.comboIdioma.addItem("")
        self.Mostrar = QtWidgets.QPushButton(self.centralwidget)
        self.Mostrar.setGeometry(QtCore.QRect(290, 90, 111, 41))
        self.Mostrar.setObjectName("Mostrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Boton.clicked.connect(self.renderizar)

        self.Mostrar.clicked.connect(self.mostrar)

        self.Reproducir.clicked.connect(self.reproducir)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Boton.setText(_translate("MainWindow", "Renderizar"))
        self.label.setText(_translate("MainWindow", "TEXTO:"))
        self.Texto.setText(_translate("MainWindow", "-------------------------------------------------"))
        self.label_3.setText(_translate("MainWindow", "AUDIO:"))
        self.Reproducir.setText(_translate("MainWindow", "Reproducir"))
        self.label_2.setText(_translate("MainWindow", "Idioma:"))
        self.comboIdioma.setItemText(0, _translate("MainWindow", "Español"))
        self.comboIdioma.setItemText(1, _translate("MainWindow", "Ingles"))
        self.comboIdioma.setItemText(2, _translate("MainWindow", "Portugues"))
        self.Mostrar.setText(_translate("MainWindow", "Mostrar"))

    def renderizar(self):

        fileout = 'ejemplo10.html'
        latex = imagen.mathmltopgn(fileout)
        print(latex)


        b = CMathML2Txt()
        filein = 'ejemplo10.html'
        b.read_file_Mathml(filein)
        idioma = self.comboIdioma.currentText()+'.template'
        print(idioma)

        b.runcmath2txt(idioma)


    def mostrar(self):

        global texto_final
        self.Imagen.setPixmap(QtGui.QPixmap("Imagen.png"))
        self.Texto.setText(texto_final)
        self.Texto.adjustSize()

    def reproducir(self):

        """
        Generación de audio

        """
        global texto_final
        s = Dispatch("SAPI.SpVoice")
        s.Speak(texto_final)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())