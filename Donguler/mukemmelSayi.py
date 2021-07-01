sayi = int(input("Bir sayi giriniz : "))
toplam = 0

for i in range(1,sayi):
    if sayi % i == 0:
        toplam += i

if toplam == sayi:
    print("{} sayisi mukemmel sayidir".format(sayi))
else:
    print("{} sayisi mukemmel sayi degildir".format(sayi))