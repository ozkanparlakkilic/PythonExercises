
import requests
import sys
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

values = soup.findAll("span",{"class":"value"})

kullanici_para_miktari = float(input("Paranızı giriniz : "))

if kullanici_para_miktari < 0:
    sys.stderr.write("Geçerli bir miktar giriniz !!!")
    sys.stderr.flush()
    sys.exit()

gram_altin = values[0].text
dolar = values[1].text
euro = values[2].text

gram_altin = gram_altin.replace(",",".")
dolar = dolar.replace(",",".")
euro = euro.replace(",",".")

print("Gram altının fiyatı : {}".format(gram_altin))
print("Doların Ederi : {}".format(dolar))
print("Euronun Ederi : {}".format(euro))
print("************************************")

print("Paranızın dolar karşılığı : {}".format(kullanici_para_miktari / float(dolar)))
print("Paranızın euro karşılığı : {}".format(kullanici_para_miktari / float(euro)))



