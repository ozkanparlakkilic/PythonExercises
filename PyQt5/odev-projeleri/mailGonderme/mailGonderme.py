
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QMessageBox

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.gonderenLabel = QLabel("Gönderen mail")
        self.parolaLabel = QLabel("Parola")
        self.gonderenMail = QLineEdit()
        self.parola = QLineEdit()
        self.gonder = QPushButton("Gönder")
        self.temizle = QPushButton("Temizle")
        self.errorMessage = QMessageBox()

        self.parola.setEchoMode(QLineEdit.Password)

        v_box = QVBoxLayout()
        h_buton_box = QHBoxLayout()
        h_gonderen_box = QHBoxLayout()
        h_parola_box = QHBoxLayout()

        h_buton_box.addWidget(self.temizle)
        h_buton_box.addWidget(self.gonder)

        h_gonderen_box.addWidget(self.gonderenLabel)
        h_gonderen_box.addWidget(self.gonderenMail)
        h_parola_box.addWidget(self.parolaLabel)
        h_parola_box.addWidget(self.parola)

        v_box.addLayout(h_gonderen_box)
        v_box.addLayout(h_parola_box)
        v_box.addLayout(h_buton_box)
        v_box.addStretch()

        h_box = QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setGeometry(100, 100, 600, 600)

        self.setWindowTitle("Oto Mail")

        self.temizle.clicked.connect(self.click)
        self.gonder.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.gonderenMail.clear()
            self.parola.clear()
        else:
            self.mail_gonder()

    def mail_gonder(self):

        try:
            with open("mail.txt", "r", encoding="utf-8") as file:
                for i in file:
                    i = i.split(",")
                    mesaj = MIMEMultipart()

                    mesaj["From"] = self.gonderenMail.text()

                    mesaj["To"] = i[1]

                    mesaj["Subject"] = "Smtp Mail Gönderme"

                    yazi = i[0] + " a stmp ile mail gönderiyorum"

                    mesaj_govdesi = MIMEText(yazi, "plain")

                    mesaj.attach(mesaj_govdesi)

                    mail = smtplib.SMTP("smtp.gmail.com", 587)
                    mail.ehlo()
                    mail.starttls()

                    mail.login(self.gonderenMail.text(),self.parola.text())
                    mail.sendmail(mesaj["From"], mesaj["To"],mesaj.as_string())

                    print("Mail Başarıyla gönderildi")
                    mail.close()
        except:
            self.errorMessage.setIcon(QMessageBox.Critical)
            self.errorMessage.setText("Hata Mesajı")
            self.errorMessage.setInformativeText('Kullanıcı adı ya da şifre yanlış')
            self.errorMessage.setWindowTitle("Error")
            self.errorMessage.exec_()

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())