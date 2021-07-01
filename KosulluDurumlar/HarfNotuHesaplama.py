
birinciVize = float(input("Birinci vizeyi giriniz : "))
ikinciVize = float(input("Ikıncı vizeyi giriniz : "))
Final = float(input("Finali giriniz : "))

Ortalama = birinciVize * 0.3 + ikinciVize * 0.3 + Final * 0.4

if Ortalama >= 90:
    print("Notunuz AA")
elif Ortalama >= 85:
    print("Notunuz BA")
elif Ortalama >= 80:
    print("Notunuz BB")
elif Ortalama >= 75:
    print("Notunuz CB")
elif Ortalama >= 70:
    print("Notunuz CC")
elif Ortalama >= 65:
    print("Notunuz DC")
elif Ortalama >= 60:
    print("Notunuz DD")
elif Ortalama >= 55:
    print("Notunuz DF")
else:
    print("Kaldınız")