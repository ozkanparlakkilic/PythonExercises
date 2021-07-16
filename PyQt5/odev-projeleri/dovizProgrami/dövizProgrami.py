

import sys
import requests
from bs4 import BeautifulSoup

from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,qApp

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.input = QLineEdit()
        self.hesapla = QPushButton("Hesapla")
        self.temizle = QPushButton("Temizle")

        self.dolarLabel = QLabel("")
        self.euroLabel = QLabel("")

        v_box = QVBoxLayout()
        h_buton_box = QHBoxLayout()

        h_buton_box.addWidget(self.temizle)
        h_buton_box.addWidget(self.hesapla)

        v_box.addWidget(self.input)
        v_box.addLayout(h_buton_box)
        v_box.addWidget(self.dolarLabel)
        v_box.addWidget(self.euroLabel)
        v_box.addStretch()

        h_box = QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setGeometry(100, 100, 300, 300)

        self.setWindowTitle("Döviz Programı")

        self.temizle.clicked.connect(self.click)
        self.hesapla.clicked.connect(self.click)

        self.show()

    def click(self):

        sender = self.sender()

        if sender.text() == "Temizle":
            self.input.clear()
            self.dolarLabel.clear()
            self.euroLabel.clear()
        else:
            self.doviz_hesapla()

    def doviz_hesapla(self):
        url = "https://www.doviz.com/"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi, "html.parser")

        values = soup.findAll("span", {"class": "value"})

        try:
            if int(self.input.text()) < 0:
                sys.stderr.write("Geçerli bir miktar giriniz !!!")
                sys.stderr.flush()
                sys.exit()
                qApp.exit()


            dolar = values[1].text
            euro = values[2].text

            dolar = dolar.replace(",", ".")
            euro = euro.replace(",", ".")

            self.dolarLabel.setText("Paranızın dolar karşılığı : {}".format(round(float(self.input.text()) / float(dolar),5)))
            self.euroLabel.setText("Paranızın euro karşılığı : {}".format(round(float(self.input.text()) / float(euro),5)))

        except:
            sys.stderr.write("Bir hata ile karşılaşıldı , Girilen miktarı kontrol ediniz !!!")
            sys.stderr.flush()
            sys.exit()
            qApp.exit()




app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())