
import requests
import sys
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

kullanici_rating = float(input("Rating giriniz : "))

if kullanici_rating < 0 or kullanici_rating > 10:
    sys.stderr.write("Geçerli bir imdb puanı giriniz !!!")
    sys.stderr.flush()
    sys.exit()

basliklar = soup.findAll("td",{"class":"titleColumn"})
ratingler = soup.findAll("td",{"class":"ratingColumn imdbRating"})

for baslik,rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if (float(rating) > kullanici_rating):
        print("Film ismi : {} Filmin Ratingi : {}".format(baslik,rating))
        print("************************")

