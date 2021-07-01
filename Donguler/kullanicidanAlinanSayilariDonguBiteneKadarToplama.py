print("********************"
      "Cikis icin 'q' ya basiniz"
      "*************************")

toplam = 0
while True:
    sayi = input("Bir sayi giriniz : ")
    if sayi == 'q':
        print("Toplam = {}".format(toplam))
        break
    elif sayi == ' ':
        print("Lütfen bir sayi giriniz")
    else:
        toplam += int(sayi)