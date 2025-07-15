import datetime
import os
import string
import random

mahasiswa_templet = {
    'nama' : 'nama',
    'nim'  : '00000000',
    'sks lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_templet.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa :")
    mahasiswa['nim'] = input("NIM Mahasiswa :")
    mahasiswa['sks_lulus'] = int(input("SKS LULUS : "))
    TAHUN_LAHIR = int(input("Masukan Tahun Lahir(YYYY) :"))
    BULAN_LAHIR = int(input("Masukan Bulan Lahir(1-12) :"))
    TANGGAL_LAHIR = int(input("Masukan Tanggal Lahir(1-31) :"))
    mahasiswa['lahir'] =  datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR) 

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':^10} {'Tanggal Lahir':^10}")  
    print("-"*60)                            

    for mahasiswa in data_mahasiswa.items():
     KEY   = mahasiswa

     NAMA  = data_mahasiswa[KEY]['nama']
     NIM   = data_mahasiswa[KEY]['nim']
     SKS   = data_mahasiswa[KEY]['sks_lulus']
     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
  
    print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10}   {LAHIR:^10}")     

    print("\n")       
    is_done = input("Mau Tambah Lagi y/n?")   
    if is_done.lower == "n":  
        break             
    
    print("\nAkhir Dari Program,Terima Kasih")

import datetime
import os
import string
import random

mahasiswa_templet = {
    'nama': 'nama',
    'nim': '00000000',
    'sks lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'DATA MAHASISWA':^30}")
    print("-" * 30)

    
    mahasiswa = dict.fromkeys(mahasiswa_templet.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM Mahasiswa : ")
    mahasiswa['sks lulus'] = int(input("SKS LULUS : "))
    
   
    TAHUN_LAHIR = int(input("Masukan Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Masukan Bulan Lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Masukan Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
    

    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa[KEY] = mahasiswa

   
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<10} {'SKS Lulus':^10} {'Tanggal Lahir':^12}")
    print("-" * 60)

    for key, mhs in data_mahasiswa.items():
        nama = mhs['nama']
        nim = mhs['nim']
        sks = mhs['sks lulus']
        lahir = mhs['lahir'].strftime("%x")
        print(f"{key:<6} {nama:<17} {nim:<10} {sks:^10} {lahir:^12}")

    
    is_done = input("\nMau Tambah Lagi (y/n)? ")
    if is_done.lower() == "n":
        break

print("\nAkhir Dari Program, Terima Kasih")


