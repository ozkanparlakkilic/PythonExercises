
import sys

from PyQt5 import QtWidgets as Qt,QtGui

def Pencere():

    app = Qt.QApplication(sys.argv)

    pencere = Qt.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 2")

    etiket1 = Qt.QLabel(pencere)
    etiket2 = Qt.QLabel(pencere)

    etiket1.setText("Burası bir yazıdır.")
    etiket1.move(200,30)

    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket2.move(65, 60)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()