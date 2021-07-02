
def harfFrekans(liste):

    harfSozluk = dict()

    for i in liste:

        if (i in harfSozluk):
            harfSozluk[i] += 1
        else:
            harfSozluk[i] = 1

    for harf, sayi in harfSozluk.items():
        print("{} harfi {} defa geciyor".format(harf, sayi))

with open("string.txt" ,"r" ,encoding="utf-8") as file:
    dosya_icerigi = file.read()
    kelime = dosya_icerigi

    liste = list()

    for i in kelime:
        for j in i:
            liste.append(j)

    harfFrekans(liste)