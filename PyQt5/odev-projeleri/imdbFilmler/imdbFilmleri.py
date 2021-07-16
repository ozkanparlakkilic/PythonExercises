
import requests
import sys
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,\
    QLabel,QMessageBox,QTextEdit

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.imdb = QLabel("imdb puani giriniz : ")
        self.imdbInput = QLineEdit()
        self.goster = QTextEdit()
        self.listele = QPushButton("Listele")
        self.temizle = QPushButton("Temizle")
        self.errorMessage = QMessageBox()

        v_box = QVBoxLayout()
        h_buton_box = QHBoxLayout()
        h_imdb_box = QHBoxLayout()

        h_buton_box.addWidget(self.temizle)
        h_buton_box.addWidget(self.listele)

        h_imdb_box.addWidget(self.imdb)
        h_imdb_box.addWidget(self.imdbInput)

        v_box.addLayout(h_imdb_box)
        v_box.addLayout(h_buton_box)
        v_box.addWidget(self.goster)
        v_box.addStretch()

        h_box = QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setGeometry(100, 100, 600, 600)

        self.setWindowTitle("Imdb Top 250")

        self.temizle.clicked.connect(self.click)
        self.listele.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.imdbInput.clear()
        else:
            self.film_listele()

    def film_listele(self):

        url = "https://www.imdb.com/chart/top/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        if float(self.imdbInput.text()) < 0 or float(self.imdbInput.text()) > 10:
            self.errorMessage.setIcon(QMessageBox.Critical)
            self.errorMessage.setText("Hata Mesajı")
            self.errorMessage.setInformativeText('Kullanıcı adı ya da şifre yanlış')
            self.errorMessage.setWindowTitle("Error")
            self.errorMessage.exec_()
        basliklar = soup.findAll("td", {"class": "titleColumn"})
        ratingler = soup.findAll("td", {"class": "ratingColumn imdbRating"})

        for baslik, rating in zip(basliklar, ratingler):
            baslik = baslik.text
            rating = rating.text

            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")

            rating = rating.strip()
            rating = rating.replace("\n", "")

            if (float(rating) > float(self.imdbInput.text())):

                self.goster.insertPlainText("Film ismi : {} Filmin Ratingi : {} \n".format(baslik, rating))
                self.goster.insertPlainText("                                                                              ")
                self.goster.insertPlainText("**************************************")
                self.goster.insertPlainText("                                                                              ")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())