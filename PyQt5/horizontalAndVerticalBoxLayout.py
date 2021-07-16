

import sys

from PyQt5 import QtWidgets as Qt

def Pencere():

    app = Qt.QApplication(sys.argv)

    okay = Qt.QPushButton("Tamam")
    cancel = Qt.QPushButton("İptal")

    h_box = Qt.QHBoxLayout()
    v_box = Qt.QVBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box.addStretch()
    v_box.addLayout(h_box)


    pencere = Qt.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()