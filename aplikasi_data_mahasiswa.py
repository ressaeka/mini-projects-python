print("="*50)
print("Aplikasi pengelolaan data sederhana")
print("="*50)
    
data_mahasiswa = []

def Tambah_data():
    Nama = input("Masukan nama mahasiswa :").strip()
    Nim = input("Masukan NIM mahasiswa :")
    Jurusan = input("Masukan jurusan mahasiswa :").strip()
    
    if not Nim.isdigit():
        print("NIM harus berupa angka")
        return
    elif len(Nim) != 10:
        print("NIM harus terdiri dari 10 digit")
        return
    elif not Nama or not Jurusan: # Memastikan nama dan jurusan tidak kosong
        print("Nama dan jurusan tidak boleh kosong")
        return
    elif any(data['Nim'] == Nim for data in data_mahasiswa):
        print("NIM sudah ada, silahkan masukan NIM yang berbeda")
        return      
   
    data_mahasiswa.append({
        "Nama": Nama,
        "Nim": Nim,
        "Jurusan": Jurusan
    })

    print("Data berhasil ditambahkan")

def Lihat_data():
    print("="*50)
    print("Daftar data mahasiswa")
    print("Masukan data yang ingin dilihat:")
    print("=" *50)
    if len(data_mahasiswa) == 0:
        print("Belum ada data yang dimasukan")
    else:
        for index, data in enumerate(data_mahasiswa, start=1):
            print(f"{index}")
            print(f"Nama: {data['Nama']}")
            print(f"NIM: {data['Nim']}")
            print(f"Jurusan: {data['Jurusan']}")

def home():
    while True:
        print("Selamat datang di home page")
        print("1. Lihat data")
        print("2. Tambah data")
        print("0. Keluar")

        pilihan = input("Masukan pilihan anda :")

        if pilihan == "2":
            Tambah_data()
        elif pilihan == "1":
            Lihat_data()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi ini")
            exit()
        else:
            print("Pilihan tidak valid, silahkan coba lagi")

home()















