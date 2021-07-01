
def mukemmelSayi():

    for i in range(1,1001):
        toplam = 0
        for j in range(1,i):

            if i % j == 0:
                toplam += j

        if toplam == i:
            print(i)

mukemmelSayi()