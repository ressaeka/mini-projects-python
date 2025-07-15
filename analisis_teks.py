import re

def hitung_karakter(teks):
    return len(teks)

def hitung_kata(teks):
    return len(teks.split())

def hitung_kalimat(teks):
    return len(re.split(r'[.?!]', teks)) - 1 if teks else 0 # handle teks kosong

def frekuensi_kata(teks):
    kata = teks.lower().split() # ubah ke huruf kecil dan split
    frekuensi = {}
    for i in kata:
        if i in frekuensi:
            frekuensi[i] += 1
        else:
            frekuensi[i] = 1
    return frekuensi

def kata_terpanjang(teks):
    kata = teks.split()
    return max(kata, key=len) if kata else "" # handle teks kosong

def kata_terpendek(teks):
    kata = teks.split()
    return min(kata, key=len) if kata else "" # handle teks kosong

def analisis_teks():
    while True:
        print("-" * 25)
        print(" Analisis Teks Sederhana ")
        print("-" * 25)
        print("\n1. Menghitung total karakter dalam teks ")
        print("2. Menghitung jumlah kata dalam teks ")
        print("3. Menghitung jumlah kalimat dalam teks ")
        print("4. Menampilkan frekuensi kemunculan kata dalam teks ")
        print("5. Menemukan kata terpanjang dalam teks ")
        print("6. Menemukan kata terpendek dalam teks ")
        print("0. Keluar\n")

        try:
            pilihan = int(input("Masukan Pilihan Anda :"))
            if pilihan < 0 or pilihan > 6:
                raise ValueError
        except ValueError:
            print("Pilihan tidak valid!!")
            continue

        teks = input("Masukan Teks :") if pilihan != 0 else "" # input teks hanya jika pilihan bukan 0

        if pilihan == 1:
            print(f"Total karakter dalam teks adalah: {hitung_karakter(teks)}")
        elif pilihan == 2:
            print(f"Jumlah kata dalam teks adalah: {hitung_kata(teks)}")
        elif pilihan == 3:
            print(f"Jumlah kalimat dalam teks adalah: {hitung_kalimat(teks)}")
        elif pilihan == 4:
            print(f"Frekuensi kemunculan kata dalam teks adalah: {frekuensi_kata(teks)}")
        elif pilihan == 5:
            print(f"Kata terpanjang dalam teks adalah: {kata_terpanjang(teks)}")
        elif pilihan == 6:
            print(f"Kata terpendek dalam teks adalah: {kata_terpendek(teks)}")
        elif pilihan == 0:
            break

if __name__ == '__main__':
    analisis_teks()
                 