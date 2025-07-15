
def tampilkan_menu():
    print("\nMenu Pengelola Kontak:")
    print("1. Tambah kontak baru")
    print("2. Lihat daftar kontak")
    print("3. Cari kontak")
    print("4. Hapus kontak")
    print("0. Keluar")

def tambah_kontak(daftar_kontak):
    nama = input("Masukkan nama kontak: ").strip()
    telepon = input("Masukkan nomor telepon: ").strip()

    if nama and telepon: # Memastikan nama dan telepon tidak kosong
        kontak_baru = {"nama": nama, "telepon": telepon}
        daftar_kontak.append(kontak_baru)
        print("Kontak berhasil ditambahkan.")
    else:
        print("Nama dan nomor telepon tidak boleh kosong.")

def lihat_daftar_kontak(daftar_kontak):
    if daftar_kontak:
        print("\nDaftar Kontak:")
        for i, kontak in enumerate(daftar_kontak):
            print(f"{i+1}. Nama: {kontak['nama']}, Telepon: {kontak['telepon']}")
    else:
        print("Daftar kontak masih kosong.")

def cari_kontak(daftar_kontak):
    nama_cari = input("Masukkan nama kontak yang ingin dicari: ").strip().lower() # Case-insensitive search
    kontak_ditemukan = False

    for kontak in daftar_kontak:
        if kontak['nama'].lower() == nama_cari: # Case-insensitive comparison
            print(f"Nama: {kontak['nama']}, Telepon: {kontak['telepon']}")
            kontak_ditemukan = True
            break # Stop searching once found

    if not kontak_ditemukan:
        print("Kontak tidak ditemukan.")

def hapus_kontak(daftar_kontak):
    nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ").strip().lower()
    kontak_ditemukan = False

    for i, kontak in enumerate(daftar_kontak):
        if kontak['nama'].lower() == nama_hapus:
            del daftar_kontak[i]
            print("Kontak berhasil dihapus.")
            kontak_ditemukan = True
            break

    if not kontak_ditemukan:
        print("Kontak tidak ditemukan.")

def main():
    daftar_kontak = []

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tambah_kontak(daftar_kontak)
        elif pilihan == '2':
            lihat_daftar_kontak(daftar_kontak)
        elif pilihan == '3':
            cari_kontak(daftar_kontak)
        elif pilihan == '4':
            hapus_kontak(daftar_kontak)
        elif pilihan == '0':
            print("TERIMAKASIH BUNG")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

    



