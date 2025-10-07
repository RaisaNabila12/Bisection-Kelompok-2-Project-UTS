# PROJECT -GROUP 2

**UTS PRAKTIKUM KOMPUTASI NUMERIK**
ANGGOTA KELOMPOK 2:
1. RAISA NABILA (2408107010037)
2. MUHAMMAD SUTAN SYARIF (2408107010102),
3. MUHAMMAD NURIL ALAM (2408107010081)
4. MUHAMMAD RAZI SIREGAR (2408107010101)
5. MIRDHA AULIA ZAHRA (2408107010115)
6. MUHAMMAD SULTHAN SHADIQ (2408107010104)

🧮 Deskripsi Program

Program ini merupakan implementasi metode Biseksi untuk mencari akar persamaan non-linear menggunakan bahasa Python.
Metode Biseksi bekerja dengan cara mencari titik tengah antara dua batas (a dan b) yang memiliki tanda nilai fungsi berlawanan, lalu mempersempit interval hingga nilai fungsi mendekati nol atau mencapai toleransi kesalahan yang ditentukan.

⚙️ Fitur Program

Pengguna dapat memasukkan fungsi f(x) secara langsung melalui input.

Dapat menentukan batas awal (a) dan batas akhir (b) interval pencarian akar.

Menentukan toleransi error (ε) untuk menghentikan iterasi.

Menampilkan hasil perhitungan berupa nilai akar hampiran, jumlah iterasi, dan nilai f(x) pada akar tersebut.

🧩 Struktur Program

main.py — menjalankan antarmuka utama program (misalnya GUI menggunakan Tkinter).

function_parse.py — berisi fungsi untuk membaca dan mengevaluasi ekspresi matematika input pengguna.

bisection_method.py — berisi algoritma utama metode Biseksi.

🧠 Alur Kerja Utama

Pengguna memasukkan fungsi dan batas interval.

Program mengevaluasi tanda f(a) dan f(b) untuk memastikan adanya akar.

Program menghitung titik tengah c = (a + b)/2.

Jika f(c) cukup mendekati nol atau error < toleransi, proses berhenti.

Jika tidak, interval diperbarui dan iterasi dilanjutkan hingga konvergen.
