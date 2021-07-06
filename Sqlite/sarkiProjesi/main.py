
from sarki import *

print(""" ****************************** 

Şarkı Programına Hoşgeldiniz

1. Şarkıları Göster

2. Şarkı Sorgula

3. Şarkı Ekle

4. Şarkı Sil

5. Şarkı Süresi Değiştir

6. Listedeki Toplam Şarkı Süresini Sorgula

Çıkmak için q'ya basın

******************************""")

sarki = Sarki_listesi()

while True:
    islem = input("Yapacağınız işlem : ")

    if islem == 'q':
        print("Program Sonlandırılıyor")
        break
    elif islem == "1":
        sarki.sarkilari_göster()
    elif islem == "2":
        isim = input("Hangi şarkıyı istiyorsunuz : ")
        print("Şarkı sorgulanıyor....")
        time.sleep(2)
        sarki.sarki_sorgula(isim)
    elif islem == "3":
        isim = input("İsim : ")
        sanatçı = input("Sanatçı : ")
        albüm = input("Albüm : ")
        prodüksiyon_şirketi = input("Prodüksiyon şirketi : ")
        şarkı_süresi = int(input("Şarkı süresi : "))

        yeni_sarki = Sarki(isim,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi)

        print("Şarkı ekleniyor....")
        time.sleep(2)
        sarki.sarki_ekle(yeni_sarki)
        print("Şarkı Eklendi....")
    elif islem == "4":
        isim = input("Hangi şarkıyı silmek istiyorsunuz : ")

        cevap = input("Emin misiniz ? (E/H) : ")

        if cevap == "E":
            print("Şarkı siliniyor....")
            time.sleep(2)
            sarki.sarki_sil(isim)
            print("Şarkı Silindi....")
    elif islem == "5":
        isim = input("Hangi şarkını süresini değiştirmek istiyorsunuz : ")
        yeni_süre = int(input("Yeni süreyi giriniz : "))

        print("Süre Değiştiriliyor....")
        time.sleep(2)
        sarki.sarki_süresi_güncelle(isim,yeni_süre)
        print("Süre Değiştirildi....")

    elif islem == "6":

        print("Bilgiler Kontrol Ediliyor....")
        time.sleep(2)
        sarki.toplam_sarki_süresi()
    else:
        print("Geçersiz işlem")