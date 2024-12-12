# Diagram Class:
#-------------------------
#|      Mahasiswa       |
#-------------------------
#| - daftar_nilai : dict |
#-------------------------
#| + tambah(nama, nilai) |
#| + tampilkan()         |
#| + hapus(nama)         |
#| + ubah(nama, nilai)   |
#-------------------------

class Mahasiswa:
    def __init__(self):
        self.daftar_nilai = {}

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa."""
        self.daftar_nilai[nama] = nilai
        print(f"Data {nama} dengan nilai {nilai} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan seluruh data mahasiswa."""
        if not self.daftar_nilai:
            print("Tidak ada data untuk ditampilkan.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.daftar_nilai.items():
                print(f"{nama}: {nilai}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        if nama in self.daftar_nilai:
            del self.daftar_nilai[nama]
            print(f"Data {nama} berhasil dihapus.")
        else:
            print(f"Data dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama, nilai):
        """Mengubah data mahasiswa berdasarkan nama."""
        if nama in self.daftar_nilai:
            self.daftar_nilai[nama] = nilai
            print(f"Data {nama} berhasil diubah menjadi {nilai}.")
        else:
            print(f"Data dengan nama {nama} tidak ditemukan.")

# Contoh penggunaan program
if __name__ == "__main__":
    mhs = Mahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Hapus data")
        print("4. Ubah data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nilai = input("Masukkan nilai: ")
            mhs.tambah(nama, nilai)
        elif pilihan == "2":
            mhs.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama yang akan dihapus: ")
            mhs.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang akan diubah: ")
            nilai = input("Masukkan nilai baru: ")
            mhs.ubah(nama, nilai)
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
