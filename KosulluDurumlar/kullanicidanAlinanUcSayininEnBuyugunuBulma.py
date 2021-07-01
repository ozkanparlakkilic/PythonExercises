
birinciSayi = int(input("Birinci sayiyi giriniz : "))
ikinciSayi = int(input("Ikinci sayiyi giriniz : "))
ucuncuSayi = int(input("Ucuncu sayiyi giriniz : "))

"""
if birinciSayi < ikinciSayi:
    if ikinciSayi < ucuncuSayi:
        print("En buyuk sayi {} sayisidir".format(ucuncuSayi))
    else:
        print("En buyuk sayi {} sayisidir".format(ikinciSayi))
else:
    if birinciSayi < ucuncuSayi:
        print("En buyuk sayi {} sayisidir".format(ucuncuSayi))
    else:
        print("En buyuk sayi {} sayisidir".format(birinciSayi))
"""

if (birinciSayi >= ikinciSayi and birinciSayi >= ucuncuSayi):
    print("En buyuk sayi {} sayisidir".format(birinciSayi))
elif (ikinciSayi >= birinciSayi and ikinciSayi >= ucuncuSayi):
    print("En buyuk sayi {} sayisidir".format(ikinciSayi))
elif (ucuncuSayi >= birinciSayi and ucuncuSayi >= ikinciSayi):
    print("En buyuk sayi {} sayisidir".format(ucuncuSayi))