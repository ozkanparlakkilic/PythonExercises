import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS kitaplik (
                   isim TEXT,
                   Yazar Text,
                   Yayinevi TEXT,
                   Sayfa_Sayisi INT)""")
    con.commit()

def add_data_table():
    cursor.execute("""INSERT INTO kitaplik VALUES("İstanbul Hatırası","Ahmet Ümit","Everest",3)""")
    con.commit()

def add_data_table_from_user_input(isim,yazar,yayinevi,sayfa_sayısı):
    cursor.execute("""INSERT INTO kitaplik VALUES(?,?,?,?)""",(isim,yazar,yayinevi,sayfa_sayısı))
    con.commit()

def all_data_select():
    cursor.execute("""SELECT * FROM kitaplik""")
    liste = cursor.fetchall()
    print("Kitaplik")
    print("----------------")
    for i in liste:
        print(i)

def all_data_format_select():
    cursor.execute("""SELECT isim,Yazar FROM kitaplik""")
    liste = cursor.fetchall()
    print("Kitaplik")
    print("----------------")
    for i in liste:
        print(i)

def all_data_format_select_where(yazar):
    cursor.execute("""SELECT * FROM kitaplik WHERE yazar = ?""",(yazar,))
    liste = cursor.fetchall()
    print("Kitaplik")
    print("----------------")
    for i in liste:
        print(i)

def update_data_table_from_user_input(old_yayinevi,new_yayinevi):
    cursor.execute("""UPDATE kitaplik set Yayinevi = ? WHERE Yayinevi = ? """, (new_yayinevi,old_yayinevi,))
    con.commit()

def delete_data_table_from_user_input(yayinevi):
    cursor.execute("""DELETE FROM kitaplik WHERE Yayinevi = ? """, (yayinevi,))
    con.commit()

"""
isim = input("İsim : ")
yazar = input("Yazar : ")
yayinevi = input("Yayinevi : ")
sayfa_sayısı = int(input("Sayfa Sayısı : "))"""

"""Create Table """
#create_table()

"""Veri ekleme"""
#add_data_table()
#add_data_table_from_user_input(isim,yazar,yayinevi,sayfa_sayısı)

"""Veri Okuma"""

#all_data_select()
#all_data_format_select()
#all_data_format_select_where("Ahmet Ümit")

"""Veri Silme ve Güncelleme"""
#update_data_table_from_user_input("Everest")
#delete_data_table_from_user_input("Everest")

con.close()