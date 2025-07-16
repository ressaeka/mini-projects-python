nilai = float(input("Masukan nilai ujian anda: "))

if 90 <= nilai <= 100:
    Kategori = "Sangat Baik (A)"
    Status = "LULUS"

elif 85 <= nilai < 90:
    Kategori = "Baik (B)"
    Status = "LULUS"
    
elif 70 <= nilai < 75:
    Kategori = "Cukup (C)"
    Status = "LULUS BERSYARAT"

elif 60 <= nilai <65 :
    Kategori = "Kurang Baik (D)"
    Status = "GAGAL"

elif 0 <= nilai < 55:
    Kategori = "Sangat Kurang (E)"
    Status = "GAGAL"

else:
    Kategori = "Tidak Valid"
    Status = "Tidak Valid"

print("Nilai anda adalah:", nilai)
print("Kategori anda adalah:", Kategori)
print("Status anda adalah:", Status)



