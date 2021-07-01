import hesapMakinesiModul as myModul

print(""" ***************************

Hesap Makinesi

Islem 1 = Toplama
Islem 2 = Carpma
Islem 3 = Cıkarma
Islem 4 = Bolme
Islem 5 = Mod Alma
Islem 6 = Us alma
Islem 7 = Kok alma

""")

while True:

    a = int(input("Birinci Sayı: "))  # Birinci Sayıyı Alıyoruz.
    b = int(input("İkinci Sayı: "))  # İkinci Sayıyı Alıyoruz.

    islem = input("İşlem Numarasını Giriniz: ")  # Buna göre koşullarımızı yazacağız.

    if islem == "q":
        print("Cıkıs Yapıldı")
        break
    if (islem == "1"):

        print("{} ile {} 'nin toplamı {} dır.".format(a,b,myModul.toplama(a,b)))
    elif (islem == "2"):

        print("{} ile {} 'nin farkı {} dır.".format(a, b,myModul.cikarma(a,b)))

    elif (islem == "3"):

        print("{} ile {} 'nin çarpımı {} dır.".format(a, b,myModul.carpma(a,b)))

    elif (islem == "4"):

        print("{} 'nın {} 'e bölümü {} dır.".format(a, b,myModul.bolme(a,b)))

    elif (islem == "5"):

        print("{} 'nın {} 'e modu {} dır.".format(a, b,myModul.modAlma(a,b)))

    elif (islem == "6"):

        print("{} 'nın {} 'e ussu {} dır.".format(a, b,myModul.usAlma(a,b)))

    elif (islem == "7"):

        print("{} 'nın {} 'e koku {} dır.".format(a, b,myModul.kokAlma(a,b)))

    else:
        """help(myModul)"""
        print("Lütfen geçerli bir işlem giriniz...")