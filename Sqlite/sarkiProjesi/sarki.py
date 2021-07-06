import sqlite3

import time

class Sarki():

    def __init__(self,isim,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi):
        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.şarkı_süresi = şarkı_süresi

    def __str__(self):
        return "Şarkı ismi = {}\n Sanatçı = {}\n Albüm = {}\n Prodüksiyon Şirketi = {}\n Şarkı Süresi = {}\n" \
            .format(self.isim, self.sanatçı, self.albüm, self.prodüksiyon_şirketi, self.şarkı_süresi)


class Sarki_listesi():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("sarki_listesi.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (isim TEXT,sanatçı TEXT,albüm TEXT,prodüksiyon_şirketi TEXT,şarkı_süresi INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarkilari_göster(self):

        sorgu = "SELECT * FROM sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Bu sarki listesi bos")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_sorgula(self,isim):

        sorgu = "SELECT * FROM sarkilar WHERE isim = ?"

        self.cursor.execute(sorgu,(isim,))

        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Bu sarki listesi bos")
        else:
            sarki = Sarki(sarkilar[0],sarkilar[1],sarkilar[2],sarkilar[3],sarkilar[4])
            print(sarki)

    def sarki_ekle(self,sarki):

        sorgu = "INSERT INTO sarkilar VALUES(?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatçı,sarki.albüm,sarki.prodüksiyon_şirketi,sarki.şarkı_süresi))

        self.baglanti.commit()

    def sarki_sil(self,isim):

        sorgu = "SELECT * FROM sarkilar WHERE = ?"

        self.cursor.execute(sorgu, (isim,))

        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Bu sarki listesi bos")
        else:
            sorgu2 = "DELETE FROM sarkilar WHERE isim = ?"

            self.cursor.execute(sorgu2,(isim,))

            self.baglanti.commit()

    def sarki_süresi_güncelle(self,isim,yeni_sarki_süresi):

        sorgu = "SELECT * FROM sarkilar WHERE isim = ?"

        self.cursor.execute(sorgu,(isim,))

        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Bu sarki listesi bos")
        else:

            sorgu2 = "UPDATE sarkilar SET şarkı_süresi = ? WHERE isim = ?"

            self.cursor.execute(sorgu2, (yeni_sarki_süresi,isim))

            self.baglanti.commit()


    def toplam_sarki_süresi(self):

        sorgu = "SELECT * FROM sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        toplam_süre = 0

        if len(sarkilar) == 0:
            print("Bu sarki listesi bos")
        else:
            for i in sarkilar:
                toplam_süre += i[4]

            print("Listedeli Toplam Süre : {}\n".format(toplam_süre))

