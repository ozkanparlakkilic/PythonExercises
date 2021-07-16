
import sys

from PyQt5 import QtWidgets as Qt

class Pencere(Qt.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazi_alani = Qt.QLineEdit()
        self.temizle = Qt.QPushButton("Temizle")
        self.yazdir = Qt.QPushButton("Yazdır")

        v_box = Qt.QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addStretch()

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)

        self.show()

    def click(self):

        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazi_alani.clear()
        else:
            print(self.yazi_alani.text())

app = Qt.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())