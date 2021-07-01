
class Hayvan():

    def __init__(self,sinirSistemi,hucreYapisi,hucreSayisi):
        self.sinirSistemi = sinirSistemi
        self.hucreYapisi = hucreYapisi
        self.hucreSayisi = hucreSayisi

    def __str__(self):
        return "Ortak Özellikler\n**************\nSinir Sistemi : {}\nHücre Yapisi: {}\nHücre Sayisi: {}\n"\
            .format(self.sinirSistemi, self.hucreYapisi,self.hucreSayisi)


class Kopek(Hayvan):
    def __init__(self, sinirSistemi, hucreYapisi, hucreSayisi,ayakSayisi,cikardigiSes):
        super().__init__(sinirSistemi,hucreYapisi,hucreSayisi)
        self.cikardigiSes = cikardigiSes
        self.ayakSayisi = ayakSayisi

    def __str__(self):
        return "Hayvan : {}\nSinir Sistemi : {}\nHücre Yapisi: {}\nHücre Sayisi: {}\nayakSayisi: {}\n"\
            .format(type(kopek).__name__,self.sinirSistemi, self.hucreYapisi,self.hucreSayisi,self.ayakSayisi)

    def Ses(self):
            print(self.cikardigiSes)

class At(Hayvan):
    def __init__(self, sinirSistemi, hucreYapisi, hucreSayisi,ayakSayisi,cikardigiSes):
        super().__init__(sinirSistemi,hucreYapisi,hucreSayisi)
        self.cikardigiSes = cikardigiSes
        self.ayakSayisi = ayakSayisi

    def __str__(self):
        return "Hayvan : {}\nSinir Sistemi : {}\nHücre Yapisi: {}\nHücre Sayisi: {}\nayakSayisi: {}\n"\
            .format(type(at).__name__,self.sinirSistemi, self.hucreYapisi,self.hucreSayisi,self.ayakSayisi)

    def Ses(self):
            print(self.cikardigiSes)

class Kus(Hayvan):
    def __init__(self, sinirSistemi, hucreYapisi, hucreSayisi,ayakSayisi,cikardigiSes):
        super().__init__(sinirSistemi,hucreYapisi,hucreSayisi)
        self.cikardigiSes = cikardigiSes
        self.ayakSayisi = ayakSayisi

    def __str__(self):
        return "Hayvan : {}\nSinir Sistemi : {}\nHücre Yapisi: {}\nHücre Sayisi: {}\nayakSayisi: {}\n"\
            .format(type(kus).__name__,self.sinirSistemi, self.hucreYapisi,self.hucreSayisi,self.ayakSayisi)

    def Ses(self):
            print(self.cikardigiSes)


print("""*******************

Hayvanlar Alemi

İşlemler ;

1. Ortak Özellikleri Göster

2. Köpeğin Bilgilerini Göster

3. Kuşun Bilgilerini Göster

4. Atın Bilgilerini Göster

5. Kopegin cikardigi ses

6. Atin cikardigi ses

7. Kusun cikardigi ses

*******************""")

hayvan = Hayvan("Gelişmiş","Ökaryot","Çok hücreli")
kopek = Kopek("Gelişmiş", "Ökaryot", "Çok hücreli",4,"Hav")
kus = Kus("Gelişmiş", "Ökaryot", "Çok hücreli",2,"Cik")
at = At("Gelişmiş", "Ökaryot", "Çok hücreli", 4, "Aağhihihih")

while True:

    islem = input("İşlemi Seçiniz : ")
    if (islem == "q"):
        print("Programdan Çıkılıyor...")
        break
    if (islem == "1"):
        print(hayvan)
    elif (islem == "2"):
        print(kopek)
    elif (islem == "3"):
        print(kus)
    elif (islem == "4"):
        print(at)
    elif (islem == "5"):
        print("Hayvan : {}".format(type(kopek).__name__))
        kopek.Ses()
    elif (islem == "6"):
        print("Hayvan : {}".format(type(at).__name__))
        at.Ses()
    elif (islem == "7"):
        print("Hayvan : {}".format(type(kus).__name__))
        kus.Ses()
    else:
        print("Geçersiz İşlem...")