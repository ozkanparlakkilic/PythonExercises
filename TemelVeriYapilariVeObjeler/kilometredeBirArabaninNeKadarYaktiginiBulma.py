kilometredeYaktigiPara = float(input("Kilometrede ne kadar yaktigini giriniz : "))
kacKilometreYol = int(input("Kac kilometre yol yaptigini giriniz : "))



print("Kilometre basina {0} kurus yakit yakarak {1} km yol giderek toplam odenmesi gereken tutar {2} TL olarak hesaplanmistir"
      .format(kilometredeYaktigiPara,kacKilometreYol,(kilometredeYaktigiPara*kacKilometreYol/100)))