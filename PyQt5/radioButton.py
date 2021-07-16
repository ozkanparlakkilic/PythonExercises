
import sys

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QRadioButton

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.radio_yazısı = QLabel("Hani dili daha çok seviyorsun ? ")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.C_Sharp = QRadioButton("C#")
        self.Php = QRadioButton("Php")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_yazısı)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.C_Sharp)
        v_box.addWidget(self.Php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Radio Button")

        self.buton.clicked.connect(lambda: self.control(self.java.isChecked(),self.python.isChecked(),
                                                        self.C_Sharp.isChecked(),self.Php.isChecked(),self.yazi_alani))

        self.show()

    def control(self,java,python,C_Sharp,Php,yazi_alani):

        if java:
            yazi_alani.setText("Java")
        elif python:
            yazi_alani.setText("Python")
        elif C_Sharp:
            yazi_alani.setText("C#")
        elif Php:
            yazi_alani.setText("Php")
        else:
            yazi_alani.setText("Herhangi bir buton seçili değil")



app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())