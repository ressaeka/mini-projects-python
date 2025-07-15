nama: str = "Budi"
usia: int = 25
tinggi_badan: float = 175.5
mahasiswa: bool = True
daftar_nama: list[str] = ["Budi", "Ani", "Citra"]
data_diri: dict[str, str] = {"nama": "Budi", "kota": "Jakarta"}

def sapa(nama: str) -> str:
    return f"Halo, {nama}!"

def hitung_luas_persegi_panjang(panjang: float, lebar: float) -> float:
    return panjang * lebar

def proses_data(data: list[int]) -> tuple[int, int]:
    total = sum(data)
    rata_rata = total / len(data)
    return total, rata_rata
    
class Person:
    def __init__(self, nama: str, usia: int):
        self.nama = nama
        self.usia = usia

    def greet(self) -> str:
        return f"Halo, nama saya {self.nama}!"

from typing import Optional, Union, Any

nama: Optional[str] = None  # nama bisa string atau None
nomor_telepon: Union[str, int] = "08123456789"  # nomor_telepon bisa string atau integer
data: Any = 123
data = "teks"  # Tidak ada error, karena tipenya Any

# Memanggil fungsi dan mencetak hasilnya
hasil_sapa = sapa("Budi")
print(hasil_sapa)

luas = hitung_luas_persegi_panjang(10.0, 5.0)
print(f"Luas persegi panjang: {luas}")

total, rata_rata = proses_data([1, 2, 3, 4, 5])
print(f"Total: {total}, Rata-rata: {rata_rata}")

person = Person("Budi", 25)
print(person.greet())

# Mencetak variabel lainnya
print(f"Nama: {nama}")
print(f"Nomor Telepon: {nomor_telepon}")
print(f"Data: {data}")
