boy = float(input("Boyunuzu metre cinsinden giriniz : "))
kilo = float(input("Kilonuzu kg cinsinden giriniz : "))

index = (kilo/(boy*boy))

if index < 18.5:
    print("Zayıf")
elif 18.5 <= index and index < 25:
    print("Normal")
elif 25 <= index and index < 30:
    print("Fazla Kilolu")
else:
    print("Obez")
