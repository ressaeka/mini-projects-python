# import math
 
# radius = float(input("Masukkan jari-jari lingkaran: "))
 
# if radius < 0:
#     print("Jari-jari tidak boleh negatif.")
# else:
#     area = math.pi * (radius ** 2)   
#     print("Luas lingkaran:", area)

import math

def luas_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    return luas

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

luas = luas_lingkaran(jari_jari)

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")