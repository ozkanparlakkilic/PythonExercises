
# Enumerate fonksiyonu ile listedeki elemanları indexkleriyle gruplayıp listeye atama
liste = ["Python","C","Java","C#"]

print(list(enumerate(liste)))

# Bir listedeki cift indeksli elemanlari yazdırma

liste = [1,2,3,4,5,6,7]

for i,j in enumerate(liste):
    if i % 2 == 0:
        print("Listedeki cift indeksli sayilar",j)
