
# Tüm listedeki elemanlari map gomulu fonksiyonu ile iki katina cikarma
def double(x):
    return x * 2

print(list(map(double,[1,2,3,4,5])))

# Lambda kullanarak listedeki her elemanin map gomulu fonksiyonu ile karesini alma

print(list(map(lambda x : x ** 2,[1,2,3,4,5,6,7,8,9,10])))

# İki listenin elemanlarini map gomulu fonksiyonu ile carpma

liste1 = [1,2,3,4,5]
liste2 = [5,10,15,20,25]

print(list(map(lambda x,y : x * y,liste1,liste2)))

# Dikdörtgen alanı hesaplama

liste = [(3,4),(10,3),(5,6),(1,9)]

def carp(liste):
    return liste[0] * liste[1]

print(list(map(carp,liste)))
