
import sys

from PyQt5 import QtWidgets as Qt

class Pencere(Qt.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.yazi_alani = Qt.QLabel("Bana Henüz tıklanmadı")
        self.buton = Qt.QPushButton("Bana tıkla")
        self.say = 0


        v_box = Qt.QVBoxLayout()

        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box = Qt.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()

    def click(self):
        self.say += 1
        self.yazi_alani.setText("Bana " + str(self.say) + " defa tıklandı")

app = Qt.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
