
#Zip fonksiyonu ile iki listeyi 2 li demet halinde tek listede içine koyma
"""
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

print(list(zip(liste1,liste2)))"""

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for isim,soyisim in zip(isimler,soyisimler):
    print(isim + " " + soyisim)