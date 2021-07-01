import random
import time

print(""" ***************************

Sayı Tahmin oyunu


1 ile 100 arasında sayıyı tahmin edin
Toplam hakkınız 10'dur

""")

rastgeleSayi = random.randint(1,100)

tahminHakki = 10
puan = 100
while True:
    tahminSayi = int(input("Tahmin sayisini giriniz : "))

    if tahminSayi == rastgeleSayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler sayiyi buldunuz")
        print("Puanınız {}".format(puan))
        break

    elif tahminSayi < rastgeleSayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek sayi deneyiniz")
        puan -= 10
        tahminHakki -= 1

    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük sayi deneyiniz")
        puan -= 10
        tahminHakki -= 1

    if tahminHakki == 0:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Sayiyi bulamadiniz")
        print("Puanınız {}".format(puan))
        break