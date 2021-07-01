sayi = input("Bir sayi giriniz : ")

liste = sayi
toplam = 0

for i in liste:
    us = len(liste)
    toplam += int(i) ** us

if toplam == int(sayi):
    print("{} sayisi armstrong sayidir".format(sayi))
else:
    print("{} sayisi armstrong sayi degildir".format(sayi))

