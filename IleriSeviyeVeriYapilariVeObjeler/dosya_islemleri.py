
class Dosya():

    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:

            dosya_icerigi = file.read()

            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)

    def tumKelimeler(self):

        kelimelerKumesi = set()

        for i in self.sade_kelimeler:
            kelimelerKumesi.add(i)

        for i in kelimelerKumesi:
            print(i)

    def kelimeSayisi(self):

        kelimelerKumesi = set()

        for i in self.sade_kelimeler:
            kelimelerKumesi.add(i)

        return print(len(kelimelerKumesi))

    def kelimeFrekansi(self):

        kelimeSozluk = dict()

        for i in self.sade_kelimeler:

            if (i in kelimeSozluk):
                kelimeSozluk[i] += 1
            else:
                kelimeSozluk[i] = 1

        for kelime,sayi in kelimeSozluk.items():

            print("{} kelimesi {} defa geciyor".format(kelime,sayi))


    def kelimeFilter(self):

        kelime = input("Kelimeyi giriniz : ")
        count = 0
        for i in self.sade_kelimeler:
            if kelime == i:
                count += 1

        if count == 0:
            print("{} kelimesi metinde hiç geçmiyor".format(kelime))
        else:
            print("{} kelimesi metinde {} defa geçiyor".format(kelime,count))

dosya = Dosya()

#dosya.tumKelimeler()

#dosya.kelimeSayisi()

#dosya.kelimeFrekansi()

#dosya.kelimeFilter()