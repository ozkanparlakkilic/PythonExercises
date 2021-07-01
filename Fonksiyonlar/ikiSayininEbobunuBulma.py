
def ebobBulma():
    sayi1 = int(input("İlk sayiyi giriniz : "))
    sayi2 = int(input("İkinci sayiyi giriniz : "))

    enBuyukOrtakBolen = 0

    if sayi1 <= sayi2:
        for i in range(1,sayi1+1):
            if sayi1 % i == 0 and sayi2 % i == 0:
                enBuyukOrtakBolen = i
    else:
        for i in range(1,sayi2+1):
            if sayi1 % i == 0 and sayi2 % i == 0:
                enBuyukOrtakBolen = i

    return enBuyukOrtakBolen


enBuyukOrtakBolen = ebobBulma()
print(enBuyukOrtakBolen)