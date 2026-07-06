from models.anggota import Anggota
from services.perpustakaan_services import PerpustakaanServices


# Penyimpanan anggota sederhana di memori (nim -> objek Anggota).
# Bukan struktur data "utama" tugas ini, hanya supaya user tidak perlu
# mengetik ulang nama & kategori anggota setiap kali mengajukan pinjam.
daftar_anggota = {}


def cari_atau_buat_anggota():
    """
    Meminta NIM anggota. Jika sudah pernah didaftarkan, pakai data lama.
    Jika belum, minta nama & kategori lalu daftarkan.
    """
    nim = input("Masukkan NIM anggota: ").strip()
    if nim in daftar_anggota:
        return daftar_anggota[nim]

    print("Anggota baru, silakan lengkapi data.")
    nama = input("Nama anggota   : ").strip()
    kategori = input("Kategori (Mahasiswa Tingkat Akhir/Mahasiswa/Dosen/Staff): ").strip()
    anggota = Anggota(nim, nama, kategori)
    daftar_anggota[nim] = anggota
    return anggota


def input_int(pesan):
    """
    Meminta input angka, mengulang jika input bukan angka.
    """
    while True:
        nilai = input(pesan).strip()
        if nilai.isdigit():
            return int(nilai)
        print("Input harus berupa angka. Coba lagi.")


def tampilkan_menu():
    print("\n" + "=" * 45)
    print("   SISTEM PERPUSTAKAAN - MENU UTAMA")
    print("=" * 45)
    print(" 1.  Tambah Buku")
    print(" 2.  Tampilkan Katalog Buku")
    print(" 3.  Cari Buku")
    print(" 4.  Hapus Buku")
    print(" 5.  Info Katalog (tinggi BST & jumlah buku)")
    print("-" * 45)
    print(" 6.  Ajukan Peminjaman (masuk Antrian)")
    print(" 7.  Tampilkan Antrian Peminjaman")
    print(" 8.  Proses Antrian -> Prioritas (Heap)")
    print(" 9.  Tampilkan Heap Prioritas")
    print("10.  Proses Peminjaman Berikutnya (dari Heap)")
    print("-" * 45)
    print("11.  Kembalikan Buku")
    print("12.  Tampilkan Riwayat Transaksi (Stack)")
    print("13.  Undo Transaksi Terakhir")
    print("-" * 45)
    print(" 0.  Keluar")
    print("=" * 45)


def main_menu():
    """
    Loop menu utama aplikasi perpustakaan berbasis Console (CLI).
    """
    service = PerpustakaanServices()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            id_buku = input("ID Buku      : ").strip().upper()
            judul = input("Judul Buku   : ").strip()
            penulis = input("Penulis      : ").strip()
            tahun = input_int("Tahun Terbit : ")
            stok = input_int("Stok Awal    : ")
            service.tambah_buku(id_buku, judul, penulis, tahun, stok)

        elif pilihan == "2":
            service.tampilkan_katalog()

        elif pilihan == "3":
            id_buku = input("ID Buku yang dicari: ").strip().upper()
            service.cari_buku(id_buku)

        elif pilihan == "4":
            id_buku = input("ID Buku yang dihapus: ").strip().upper()
            service.hapus_buku(id_buku)

        elif pilihan == "5":
            service.info_katalog()

        elif pilihan == "6":
            anggota = cari_atau_buat_anggota()
            id_buku = input("ID Buku yang dipinjam: ").strip().upper()
            service.ajukan_peminjaman(anggota, id_buku)

        elif pilihan == "7":
            service.tampilkan_antrian()

        elif pilihan == "8":
            service.proses_antrian_ke_prioritas()

        elif pilihan == "9":
            service.tampilkan_prioritas()

        elif pilihan == "10":
            service.proses_peminjaman_berikutnya()

        elif pilihan == "11":
            anggota = cari_atau_buat_anggota()
            id_buku = input("ID Buku yang dikembalikan: ").strip().upper()
            service.kembalikan_buku(anggota, id_buku)

        elif pilihan == "12":
            service.tampilkan_riwayat()

        elif pilihan == "13":
            service.undo_transaksi_terakhir()

        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak dikenali, coba lagi.")


if __name__ == "__main__":
    main_menu()
