
import os

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/OzkanParlakkilic/Desktop"):
    for i in dosya_isimleri:
        if i.endswith(".txt") or i.endswith(".mp4"):
            print(i)