
def takimlaraAyir(satir):

    satir = satir[:-1]
    liste = satir.split(",")
    takimName = liste[1]
    takimName = takimName.strip()

    if takimName == "Galatasaray":
        with open("gs.txt", "a", encoding="utf-8") as gsFile:
            gsFile.write(satir+"\n")
    elif takimName == "Fenerbahçe":
        with open("fb.txt", "a", encoding="utf-8") as fbFile:
            fbFile.write(satir+"\n")
    else:
        with open("bjk.txt", "a", encoding="utf-8") as bjkFile:
            bjkFile.write(satir+"\n")

with open("futbolcular.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    for i in file:
        takimlaraAyir(i)



