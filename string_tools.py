def main():
    teks = input("Masukkan teks: ")

    while True:
        print("\nOperasi String:")
        print("1. Hitung panjang teks")
        print("2. Ubah ke huruf besar")
        print("3. Ubah ke huruf kecil")
        print("4. Hapus spasi putih")
        print("5. Ganti substring (berulang)")
        print("6. Pisahkan teks (berulang)")
        print("7. Cari substring (berulang)")
        print("8. Cek awalan")
        print("9. Cek akhiran")
        print("10. Gabungkan list kata (berulang)")
        print("11.kembali ke menu utama")
        print("0.keluar")

        pilihan = input("Masukkan pilihan (1-10 atau 0 untuk keluar): ")

        if pilihan == '0':
            break
            

        elif pilihan == '1':
            print(f"Panjang teks: {len(teks)}")

        elif pilihan == '2':
            print(f"Teks huruf besar: {teks.upper()}")

        elif pilihan == '3':
            print(f"Teks huruf kecil: {teks.lower()}")

        elif pilihan == '4':
            print(f"Teks bersih: {teks.strip()}")

        elif pilihan == '5':
            while True:
                old = input("Masukkan substring yang ingin diganti (atau 'kembali'): ")
                if old.lower() == 'kembali':
                    break
                new = input("Masukkan substring pengganti: ")
                teks = teks.replace(old, new)
                print(f"Teks baru: {teks}")

        elif pilihan == '6':
            while True:
                separator = input("Masukkan pemisah (atau 'kembali'): ")
                if separator.lower() == 'kembali':
                    break
                daftar_kata = teks.split(separator)
                print("Daftar kata:")
                for kata in daftar_kata:
                    print(kata)

        elif pilihan == '7':
            while True:
                substring = input("Masukkan substring yang ingin dicari (atau 'kembali'): ")
                if substring.lower() == 'kembali':
                    break
                posisi = teks.find(substring)
                if posisi != -1:
                    print(f"Substring ditemukan di posisi {posisi}")
                else:
                    print("Substring tidak ditemukan")

        elif pilihan == '8':
            prefix = input("Masukkan awalan yang ingin dicek: ")
            print(f"Teks dimulai dengan '{prefix}': {teks.startswith(prefix)}")

        elif pilihan == '9':
            suffix = input("Masukkan akhiran yang ingin dicek: ")
            print(f"Teks diakhiri dengan '{suffix}': {teks.endswith(suffix)}")

        elif pilihan == '10':
            while True:
                kata_kata = input("Masukkan kata-kata (dipisahkan spasi) (atau 'kembali'): ")
                if kata_kata.lower() == 'kembali':
                    break
                kata_kata = kata_kata.split()
                kalimat = " ".join(kata_kata)
                print(f"Kalimat: {kalimat}")

        elif pilihan == "11":
            main()

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()