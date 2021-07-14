
def ekstra(func):
    def wrapper(sayılar):
        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:
            if sayı % 2 == 0:
                çift_sayılar += 1
                çiftler_toplamı += sayı
            else:
                tek_sayılar += 1
                tekler_toplamı += sayı

        print("Teklerin Ortalaması : {} , Çiftlerin Ortalaması : {}"\
              .format(tekler_toplamı/tek_sayılar,çiftler_toplamı/çift_sayılar))

        func(sayılar)
    return wrapper

@ekstra
def ortalamabul(sayılar):

    toplam = 0

    for sayı in sayılar:
        toplam += sayı

    print("Genel Ortalama : ",toplam / len(sayılar))

ortalamabul([1,2,3,4,34,60,63,32,100,105])