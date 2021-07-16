
import sys
import sqlite3
from PyQt5 import QtWidgets as Qt

class Pencere(Qt.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):

        baglanti = sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Uyeler (kullanici_adi TEXT,parola TEXT)")

        baglanti.commit()

    def kullaniciKontrol(self,adi,parola):

        self.cursor.execute("SELECT * FROM Uyeler WHERE kullanici_adi = ? and parola = ?", (adi, parola))
        data = self.cursor.fetchall()

        return data

    def kullaniciKayit(self,kullanici_adi,parola):

        self.cursor.execute("INSERT INTO Uyeler VALUES(?,?)",(kullanici_adi,parola))
        self.baglanti.commit()

    def init_ui(self):

        self.kullanici_adi = Qt.QLineEdit()
        self.parola = Qt.QLineEdit()
        self.parola.setEchoMode(Qt.QLineEdit.Password)
        self.giris = Qt.QPushButton("Giriş Yap")
        self.kayit = Qt.QPushButton("Kayıt ol")
        self.yazi_alani = Qt.QLabel("")

        v_box = Qt.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit)

        h_box = Qt.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")

        self.giris.clicked.connect(self.login)
        self.kayit.clicked.connect(self.register)

        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        kontrol = self.kullaniciKontrol(adi,par)

        if len(kontrol) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyiniz")
        else:
            self.yazi_alani.setText("Hoşgeldiniz " + adi)

    def register(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        kontrol = self.kullaniciKontrol(adi, par)

        if len(kontrol) == 0:
            self.kullaniciKayit(adi, par)
        else:
            self.yazi_alani.setText("Bu kullanıcı ismi zaten var")

app = Qt.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())