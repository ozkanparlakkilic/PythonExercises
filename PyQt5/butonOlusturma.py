
import sys

from PyQt5 import QtWidgets as Qt

def Pencere():

    app = Qt.QApplication(sys.argv)

    pencere = Qt.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 3")

    buton = Qt.QPushButton(pencere)

    buton.setText("Tıklayınız")

    etiket = Qt.QLabel(pencere)

    etiket.setText("Merhaba Dünya")

    etiket.move(200,30)
    buton.move(200,60)

    pencere.setGeometry(100, 100, 500, 500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()