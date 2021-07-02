from functools import reduce

# Reduce fonksiyonu ile listenin elemanlarini toplama

print(reduce(lambda x,y : x + y,[12,18,20,10]))

# Reduce fonksiyonu ile faktoriyel hesaplama
sayi = int(input("Faktoriyelinin hesaplanmasini istediginiz sayiyi giriniz : "))

liste = []

for i in range(1,sayi+1):
    liste.append(i)

print(reduce(lambda x,y : x * y,liste))

# Reduce fonksiyonu ile listenin maximum degerini bulma

def maximum(x,y):
    if x > y:
        return x
    else:
        return y

print(reduce(maximum,[20,100,32,65,78]))

# Listedeki çift sayıları filter ile alıp reduce ile toplatıyoruz
liste = [1,2,3,4,5,6,7,8,9,10]

filterListe = list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8,9,10]))
print(reduce(lambda x,y : x + y,filterListe))