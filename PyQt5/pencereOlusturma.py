
import sys

from PyQt5 import QtWidgets as Qt

def Pencere():

    app = Qt.QApplication(sys.argv)

    pencere = Qt.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 1")

    pencere.show()

    sys.exit(app.exec_())


Pencere()