# Lab7 Mata Kuliah Program Komputer + Praktek

Program di atas adalah program Python sederhana untuk mengelola daftar nilai mahasiswa menggunakan konsep class dan object. Berikut adalah rincian penjelasannya:

1. Struktur Program
Program ini terdiri dari satu class bernama Mahasiswa, yang bertugas mengelola data mahasiswa seperti nama dan nilai mereka. Ada juga logika utama di bawah blok if __name__ == "__main__" untuk menjalankan aplikasi secara interaktif.

2. Class Mahasiswa
Class ini berisi atribut dan metode sebagai berikut:

A. Atribut:

- data: Sebuah dictionary (dict) untuk menyimpan data mahasiswa.
- Key: Nama mahasiswa (str).
- Value: Nilai mahasiswa (float).

B. Method:

- __init__():
    > Konstruktor untuk menginisialisasi atribut data sebagai dictionary kosong.
- tambah(nama, nilai):
    > Menambahkan data mahasiswa ke dalam atribut data.
    > Jika mahasiswa sudah ada, nilainya akan diperbarui secara otomatis.
- tampilkan():
    > Menampilkan semua data mahasiswa dalam format yang rapi.
    > Jika tidak ada data, mencetak pesan "Tidak ada data mahasiswa."
- hapus(nama):
    > Menghapus data mahasiswa berdasarkan nama.
    > Jika nama tidak ditemukan, mencetak pesan "Data tidak ditemukan."
- ubah(nama, nilai):
    > Mengubah nilai mahasiswa berdasarkan nama.
    > Jika nama tidak ditemukan, mencetak pesan "Data tidak ditemukan."


3. Program Utama:

   A) Menu Utama
      Menampilkan pilihan operasi
       1. Tambah Data
       2. Tampilkan Data
       3. Hapus Data
       4. Ubah Data
       5. Keluar dari program.

    B) Operasi
       - Tambah Data:
         > Meminta input nama dan nilai mahasiswa untuk ditambahkan. 
       - Tampilkan Data:
         > Menampilkan seluruh daftar mahasiswa dan nilai mereka.
       - Hapus Data:
         > Meminta input nama mahasiswa untuk menghapus data mereka.
       - Ubah Data:
         > Meminta input nama mahasiswa dan nilai baru untuk memperbarui data mereka.
       - Keluar:
         > Mengakhiri program.
   C) Validasi Input:
      - Program memeriksa validitas input (misalnya, apakah nama ditemukan atau tidak) dan memberikan pesan yang sesuai.
  
Diagram Class:
+---------------------+
|      Mahasiswa      |
+---------------------+
| - data: dict        |
+---------------------+
| + __init__() : None                         |
| + tambah(nama: str, nilai: float) : None    |
| + tampilkan() : None                        |
| + hapus(nama: str) : None                   |
| + ubah(nama: str, nilai: float) : None      |
+---------------------+


Beberapa Contoh Hasil Output dari Program:
<img width="959" alt="image" src="https://github.com/user-attachments/assets/6ff961c2-cc20-4fe2-9aea-a55987b3964a" />

<img width="957" alt="image" src="https://github.com/user-attachments/assets/e5f3e4c0-6fde-4fef-b5ee-ac60e7c6a836" />

<img width="959" alt="image" src="https://github.com/user-attachments/assets/1483b5c7-28da-4ec0-9b77-0b4f34826f86" />

# FLowChart

![image](https://github.com/user-attachments/assets/ee6f3368-9037-41bb-8a03-98f8b7575e80)



