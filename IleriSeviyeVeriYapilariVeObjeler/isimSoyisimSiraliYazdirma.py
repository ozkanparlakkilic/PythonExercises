
liste1 = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
liste2 = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste3 = list()

for isim,soyisim in zip(liste1,liste2):
    fullname = isim + " " + soyisim
    liste3.append(fullname)

liste3.sort()
for i in liste3:
    print(i)

