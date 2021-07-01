kenar = int(input("Ucgense 3 giriniz , Dortgense 4 giriniz : "))

if kenar == 4:
    birinciKenar = int(input("Birinci kenari giriniz : "))
    ikinciKenar = int(input("Ikinci kenari giriniz : "))
    ucuncuKenar = int(input("Ucuncu kenari giriniz : "))
    dorduncuKenar = int(input("Dorduncu kenari giriniz : "))

    if birinciKenar == ikinciKenar and ikinciKenar == ucuncuKenar and ucuncuKenar == dorduncuKenar:
        print("Bu bir karedir")
    elif (birinciKenar == ikinciKenar and ucuncuKenar == dorduncuKenar) or \
            (birinciKenar == ucuncuKenar and ikinciKenar == dorduncuKenar) or \
            (birinciKenar == dorduncuKenar and ikinciKenar == ucuncuKenar):
        print("Bu bir dikdörtgendir")
    else:
        print("Bu bir dörtgendir")
elif kenar == 3:
    birinciKenar = int(input("Birinci kenari giriniz : "))
    ikinciKenar = int(input("Ikinci kenari giriniz : "))
    ucuncuKenar = int(input("Ucuncu kenari giriniz : "))

    if birinciKenar == ikinciKenar and ikinciKenar == ucuncuKenar:
        print("Bu bir eskaner ucgendir")
    elif (birinciKenar == ikinciKenar) or (birinciKenar == ucuncuKenar) or (ikinciKenar == ucuncuKenar):
        print("Bu bir ikizkenar ucgendir")
    elif abs(ikinciKenar - ucuncuKenar) <= birinciKenar < (ikinciKenar + ucuncuKenar) or \
            abs(birinciKenar - ucuncuKenar) <= ikinciKenar < (birinciKenar + ucuncuKenar) or \
            abs(ikinciKenar - birinciKenar) <= ucuncuKenar < (ikinciKenar + birinciKenar):
        print("Bu bir ucgendir")
    else:
        print("Bu ucgen cizilemez")
else:
    print("3 veya 4 kenar giriniz")