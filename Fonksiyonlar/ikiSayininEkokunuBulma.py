
def ekokBulma():
    sayi1 = int(input("İlk sayiyi giriniz : "))
    sayi2 = int(input("İkinci sayiyi giriniz : "))

    temp1 = sayi1
    temp2 = sayi2
    enKucukOrtakKat = 0

    if sayi1 == sayi2:
        enKucukOrtakKat = sayi1

    elif temp1 < temp2:
        while temp1 != temp2:
            if temp1 < temp2:
                temp1 += sayi1
            else:
                temp2 += sayi2

        enKucukOrtakKat = temp1

    else:
        while temp1 != temp2:
            if temp1 < temp2:
                temp1 += sayi1
            else:
                temp2 += sayi2

        enKucukOrtakKat = temp1
    return enKucukOrtakKat


enKucukOrtakKat = ekokBulma()
print(enKucukOrtakKat)