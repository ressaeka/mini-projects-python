def tampilkan_menu():
    print("\nMenu Operasi:")
    print("1. Tambah tugas baru")
    print("2. Lihat daftar tugas")
    print("3. Tandai tugas sebagai selesai")
    print("4. Hapus tugas")
    print("0. Keluar")

def tambah_tugas(daftar_tugas):
    deskripsi = input("Masukkan deskripsi tugas: ").strip()
    if deskripsi:  # Pastikan deskripsi tidak kosong
        tugas_baru = {"deskripsi": deskripsi, "status": False}
        daftar_tugas.append(tugas_baru)
        print("Tugas berhasil ditambahkan.")
    else:
        print("Deskripsi tugas tidak boleh kosong.")

def lihat_daftar_tugas(daftar_tugas):
    if daftar_tugas:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(daftar_tugas):
            status = "Selesai" if tugas["status"] else "Belum Selesai"
            print(f"{i+1}. {tugas['deskripsi']} ({status})")
    else:
        print("Daftar tugas masih kosong.")

def tandai_tugas_selesai(daftar_tugas):
    if daftar_tugas:
        lihat_daftar_tugas(daftar_tugas)
        try:
            nomor_tugas = int(input("Masukkan nomor tugas yang ingin ditandai selesai: "))
            if 1 <= nomor_tugas <= len(daftar_tugas):
                daftar_tugas[nomor_tugas-1]["status"] = True
                print("Tugas berhasil ditandai selesai.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input nomor tugas tidak valid.")
    else:
        print("Daftar tugas masih kosong.")

def hapus_tugas(daftar_tugas):
    if daftar_tugas:
        lihat_daftar_tugas(daftar_tugas)
        try:
            nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor_tugas <= len(daftar_tugas):
                del daftar_tugas[nomor_tugas-1]
                print("Tugas berhasil dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input nomor tugas tidak valid.")
    else:
        print("Daftar tugas masih kosong.")

def main():
    daftar_tugas = []

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tambah_tugas(daftar_tugas)
        elif pilihan == '2':
            lihat_daftar_tugas(daftar_tugas)
        elif pilihan == '3':
            tandai_tugas_selesai(daftar_tugas)
        elif pilihan == '4':
            hapus_tugas(daftar_tugas)
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()