age = float(input("Masukan umur anda : "))

if  40 <= age <= 100:
    kategori = "Lansia"
    status = "Anda sudah lansia"

elif 18 <= age:
    kategori = "Dewasa"
    status = "Anda sudah dewasa"

elif 13 <= age < 18 :
    kategori = "Anak Demaja"
    status = "Anda masih anank remaja"

elif 6 <= age < 13 :
    kategori = "Anak Kecil"
    status = "Anda masih anak kecil"

elif 0 <= age < 6 :
    kategori = "Bayi"
    status = "Anda masih bayi"

else:
    kategori = "tidak valid"
    status = "Umur tidak valid"

print(f"Umur anda adalah: {age}")
print(f"Kategori anda adalah: {kategori}")
print(f"Status anda adalah: {status}")





    
