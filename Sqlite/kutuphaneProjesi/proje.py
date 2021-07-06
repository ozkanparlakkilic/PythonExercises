from kutuphane import *

print(""" ****************************** 

Kütüphane Programına Hoşgeldiniz

1. Kitapları Göster

2. Kitap Sorgula

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yükselt

Çıkmak için q'ya basın

******************************""")

kütüphane = Kütüphane()

while True:
    islem = input("Yapacağınız işlem : ")

    if islem == 'q':
        print("Program Sonlandırılıyor")
        break
    elif islem == "1":
        kütüphane.kitaplari_göster()
    elif islem == "2":
        isim = input("Hangi kitabı istiyorsunuz : ")
        print("Kitap sorgulanıyor....")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("İsim : ")
        yazar = input("Yazar : ")
        yayinevi = input("Yayinevi : ")
        tür = input("Tür : ")
        baskı = int(input("Baskı : "))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tür,baskı)

        print("Kitap ekleniyor....")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi....")
    elif islem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz : ")

        cevap = input("Emin misiniz ? (E/H) : ")

        if cevap == "E":
            print("Kitap siliniyor....")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap Silindi....")
    elif islem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz : ")

        print("Baskı Yükseltiliyor....")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı Yükseltildi....")
    else:
        print("Geçersiz işlem")