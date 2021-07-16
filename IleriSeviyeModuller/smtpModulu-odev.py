
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

try:
    with open("mailGonderme/mail.txt", "r", encoding="utf-8") as file:
        for i in file:
            i = i.split(",")
            mesaj = MIMEMultipart()

            mesaj["From"] = "prlkklc@gmail.com"
            mesaj["To"] = i[1]

            mesaj["Subject"] = "Smtp Mail Gönderme"

            yazi = i[0] + " a stmp ile mail gönderiyorum"

            mesaj_govdesi = MIMEText(yazi, "plain")

            mesaj.attach(mesaj_govdesi)

            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("prlkklc@gmail.com", "159753ts")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

            print("Mail Başarıyla gönderildi")
            mail.close()
except:
    sys.stderr.write("Bir hata ile karşılaşıldı !!!")
    sys.stderr.flush()
    


