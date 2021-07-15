
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "gönderen mail"

mesaj["To"] = "alıcı mail"

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """

Smtp ile mail gönderiyorum

Özkan Parlakkılıç

"""

mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("kendi mailinizi giriniz","parola giriniz")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla gönderildi")
    mail.close()
except:
    sys.stderr.write("Bir hata ile karşılaşıldı !!!")
    sys.stderr.flush()