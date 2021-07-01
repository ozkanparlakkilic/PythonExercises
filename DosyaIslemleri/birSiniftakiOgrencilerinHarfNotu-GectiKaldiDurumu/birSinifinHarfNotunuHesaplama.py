
def notHesapla(satir):
    satir = satir[:-1]

    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1*0.3 + not2*0.3 + not3*0.4

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "DF"
    else:
        harf = "FF"

    return isim + "--------------------> " + harf + "\n"

def kalanlarGecenler(satir):

    satir = satir[:-1]
    liste = i.split(">")

    harf_notu = liste[1]
    harf_notu = harf_notu.strip()

    if harf_notu == "FF":
        with open("kalanlar.txt", "a", encoding="utf-8") as kalanlarFile:
            kalanlarFile.write(satir+"\n")
    else:
        with open("gecenler.txt", "a", encoding="utf-8") as gecenlerFile:
            gecenlerFile.write(satir+"\n")

with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        eklenecekler_listesi.append(notHesapla(i))

    with open("notlar.txt", "w", encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)

            kalanlarGecenler(i)


