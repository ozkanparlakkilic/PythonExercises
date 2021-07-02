
with open("mailler.txt" ,"r" ,encoding="utf-8") as file:
    dosya_icerigi = file.readlines()
    text = dosya_icerigi

    liste = list()

    formatListe = list()

    for i in text:
        i = i.strip("\n")
        liste.append(i)

    for i in liste:
        if i.endswith(".com") and i.find("@") != -1:
                print(i)

