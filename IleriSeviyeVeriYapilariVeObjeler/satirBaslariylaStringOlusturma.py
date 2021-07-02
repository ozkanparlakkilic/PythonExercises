
with open("siir.txt" ,"r" ,encoding="utf-8") as file:
    dosya_icerigi = file.readlines()
    text = dosya_icerigi

    liste = list()

    capitalListe = list()

    for i in text:
        i = i.strip("\n")
        liste.append(i)

    for i in liste:
        capitalListe.append(i[0])

    for i in capitalListe:
        print(i,end="")