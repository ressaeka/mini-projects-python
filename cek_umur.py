import datetime as dt

print("silakan masukan tanggal lahir anda,\nbulan,dan tahun lahir\n")
tanggal =int(input("masukan tanggal \t:"))
bulan =int(input("masukan bulan\t\t:"))
tahun =int(input("masukan tahun\t\t:"))

tanggal_lahir = dt.date (tahun,bulan,tanggal)
print(f"tanggal lahir anda\t:{tanggal_lahir}")
print(f"harinya adalah\t\t:{tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal\t:{hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 
umur_bulan_sisa = (umur_hari.days % 365)

print(f"harinya adalah\t\t:{tanggal_lahir:%A}")
print(f"umurnya adalah\t\t:{umur_tahun} tahun")