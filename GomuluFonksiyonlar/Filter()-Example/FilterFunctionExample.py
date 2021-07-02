
# Filter fonksiyonu ile listedeki çift sayilari ekrana basma
print(list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8,9,10])))

# Filter fonksiyonu ile listedeki asal sayiları ekrana basma

def asalSayi(x):
    if x == 1:
        return False

    count = 0
    for i in range(2,x+1):
        if x % i == 0:
            count += 1

    if count == 1:
        return True
    else:
        return False


print(list(filter(asalSayi,[2,4,5,34,6,7,89,67,13,29,45,65,67,98])))
# Sorted fonksiyonu ile sıralı olarak listeye basılmıştır
print(sorted(list(filter(asalSayi,[2,4,5,34,6,7,89,67,13,29,45,65,67,98]))))

#Listeden ucgen cizilebilen degerleri alma
def ucgenmi(liste):

    if abs(liste[1] - liste[2]) < liste[0] < liste[1] + liste[2] and \
            abs(liste[0] - liste[2]) < liste[1] < liste[0] + liste[2] and \
            abs(liste[1] - liste[0]) < liste[2] < liste[1] + liste[0]:

        return liste

liste = [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ucgenmi,liste)))