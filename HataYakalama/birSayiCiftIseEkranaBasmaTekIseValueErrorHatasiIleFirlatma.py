
def ciftmiTekmi(sayi):
    if sayi % 2 == 0:
        return print(sayi)
    else:
        raise ValueError("Bu sayi Tek'dir")


liste = [2,4,5,34,7,53,78,45,31,75]

for i in liste:
    try:
        ciftmiTekmi(i)
    except ValueError:
        print("Bu sayi tekdir")

