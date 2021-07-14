

def mükemmel_sayi(func):
    def wrapper(sayılar):
        toplam = 0

        for sayı in sayılar:
            for i in range(1,sayı):
                if sayı % i == 0:
                    toplam += i

            if toplam == sayı:
                print("Mukemmel sayi : {}".format(sayı))
            toplam = 0
        func(sayılar)
    return wrapper


@mükemmel_sayi
def asal_bul(sayılar):

    count = 0
    for sayi in sayılar:
        for i in range(1,sayi+1):
            if sayi % i == 0:
                count += 1

        if count == 2:
            print("Asal sayı : {}".format(sayi))
        count = 0

asal_bul(range(1,1001))
