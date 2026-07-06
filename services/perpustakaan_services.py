from structures.bst import BinarySearchTree
from structures.queue import Queue
from structures.stack import Stack
from structures.binary_heap import BinaryHeap

from models.buku import Buku
from models.transaksi import Transaksi

class PerpustakaanServices:
    def __init__(self):
        # Struktur Data

        # BST -> katalog buku
        self.katalog = BinarySearchTree()

        # Queue -> antrian peminjaman
        self.antrian = Queue()

        # Heap -> prioritas peminjaman
        self.prioritas = BinaryHeap(mode="min")

        # Stack -> riwayat transaksi
        self.riwayat = Stack()

        # Counter agar urutan pada heap tetap FIFO
        # jika prioritasnya sama
        self.counter = 0

    # MENU 1
    # TAMBAH BUKU
   
    def tambah_buku(self, id_buku, judul, penulis, tahun, stok):
        """
        Menambahkan buku baru ke BST.
        """

        buku = Buku(
            id_buku,
            judul,
            penulis,
            tahun,
            stok
        )

        berhasil = self.katalog.insert(buku)

        if berhasil:
            print("\nBuku berhasil ditambahkan.")
        else:
            print("\nID buku sudah digunakan.")

       # MENU 2
    # TAMPILKAN KATALOG
   
    def tampilkan_katalog(self):
        """
        Menampilkan seluruh buku menggunakan
        traversal Inorder.
        """

        data = self.katalog.inorder()

        if len(data) == 0:
            print("\nKatalog masih kosong.")
            return

        print("\n========== KATALOG BUKU ==========\n")

        for buku in data:
            print(buku)

       # MENU 3
    # CARI BUKU
   
    def cari_buku(self, id_buku):
        """
        Mencari buku berdasarkan ID.
        """

        buku = self.katalog.search(id_buku)

        if buku is None:
            print("\nBuku tidak ditemukan.")
            return

        print("\n===== HASIL PENCARIAN =====")
        print(buku)

       # MENU 4
    # HAPUS BUKU
   
    def hapus_buku(self, id_buku):
        """
        Menghapus buku dari BST.
        """

        buku = self.katalog.search(id_buku)

        if buku is None:
            print("\nBuku tidak ditemukan.")
            return

        self.katalog.delete(id_buku)

        print(f"\nBuku '{buku.judul}' berhasil dihapus.")

    # MENU 5
    # INFO KATALOG
   
    def info_katalog(self):
        """
        Menampilkan informasi BST.
        """

        print("\n========== INFO KATALOG ==========\n")

        print("Jumlah Buku :", self.katalog.count_nodes())
        print("Tinggi BST  :", self.katalog.height())

        print("\nTraversal Level Order (BFS)\n")

        data = self.katalog.level_order()

        if len(data) == 0:
            print("BST kosong.")
            return

        for buku in data:
            print(buku)

    # MENU 6
    # AJUKAN PEMINJAMAN (QUEUE)

    def ajukan_peminjaman(self, anggota, id_buku):
        """
        Menambahkan permintaan peminjaman ke Queue.
        """

        data = {
            "anggota": anggota,
            "id_buku": id_buku,
        }

        self.antrian.enqueue(data)

        print(f"\n{anggota.nama} berhasil masuk ke antrian.")

    # MENU 7
    # TAMPILKAN ANTRIAN

    def tampilkan_antrian(self):

        print("\n========== ANTRIAN PEMINJAMAN ==========\n")

        if self.antrian.is_empty():
            print("Antrian kosong.")
            return

        nomor = 1

        for data in self.antrian.items:

            anggota = data["anggota"]

            print(
                f"{nomor}. "
                f"{anggota.nama} "
                f"({anggota.kategori}) "
                f"-> Buku {data['id_buku']}"
            )

            nomor += 1

    # HELPER
    # PRIORITAS ANGGOTA

    def _nilai_prioritas(self, kategori):
        """
        Semakin kecil nilainya,
        semakin tinggi prioritasnya.
        """

        kategori = kategori.lower()

        if kategori == "dosen":
            return 1
        
        elif kategori == "staff":
            return 2

        elif kategori == "mahasiswa tingkat akhir":
            return 3

        elif kategori == "mahasiswa":
            return 4

        return 4

    # MENU 8
    # QUEUE -> HEAP

    def proses_antrian_ke_prioritas(self):
        """
        Memindahkan seluruh Queue ke Heap.
        """

        if self.antrian.is_empty():
            print("\nAntrian kosong.")
            return

        data = self.antrian.dequeue()

        anggota = data["anggota"]


        prioritas = self._nilai_prioritas(
        anggota.kategori
        )

        self.counter += 1

        key = (
            prioritas,
            self.counter
        )

        self.prioritas.insert(
            key,
            data
        )


        print(
            f"\n{anggota.nama} data berhasil dipindahkan "
            f"ke Heap Prioritas."
        )

    # MENU 9
    # TAMPILKAN HEAP

    def tampilkan_prioritas(self):

        print("\n========== HEAP PRIORITAS ==========\n")

        if self.prioritas.is_empty():
            print("Heap kosong.")
            return

        self.prioritas.display_tree()

    # MENU 10
    # PROSES PEMINJAMAN

    def proses_peminjaman_berikutnya(self):
        """
        Heap
            ↓
        BST
            ↓
        Stack
        """

        if self.prioritas.is_empty():
            print("\nTidak ada data pada Heap.")
            return

        key, data = self.prioritas.extract()

        anggota = data["anggota"]
        id_buku = data["id_buku"]

        buku = self.katalog.search(id_buku)

        if buku is None:

            print("\nBuku tidak ditemukan.")
            return

        if not buku.dipinjam():

            print("\nStok buku habis.")
            return

        transaksi = Transaksi(
            anggota,
            buku,
            "Peminjaman"
        )

        self.riwayat.push(transaksi)

        print("\n===== PEMINJAMAN BERHASIL =====\n")

        print(f"Nama      : {anggota.nama}")
        print(f"Kategori  : {anggota.kategori}")
        print(f"Buku      : {buku.judul}")
        print(f"Sisa Stok : {buku.stok}")
    
    # MENU 11
    # KEMBALIKAN BUKU

    def kembalikan_buku(self, anggota, id_buku):
        """
        Mengembalikan buku:
        BST -> tambah stok
        Stack -> simpan riwayat pengembalian
        """

        buku = self.katalog.search(id_buku)

        if buku is None:
            print("\nBuku tidak ditemukan.")
            return

        buku.dikembalikan()

        transaksi = Transaksi(
            anggota,
            buku,
            "Pengembalian"
        )

        self.riwayat.push(transaksi)

        print("\n===== PENGEMBALIAN BERHASIL =====")
        print(f"Nama      : {anggota.nama}")
        print(f"Buku      : {buku.judul}")
        print(f"Stok Baru : {buku.stok}")

    # MENU 12
    # TAMPILKAN RIWAYAT

    def tampilkan_riwayat(self):
        """
        Menampilkan isi Stack.
        """

        print("\n========== RIWAYAT TRANSAKSI ==========\n")

        if self.riwayat.is_empty():
            print("Belum ada transaksi.")
            return

        self.riwayat.display()

    # MENU 13
    # UNDO TRANSAKSI TERAKHIR

    def undo_transaksi_terakhir(self):
        """
        Membatalkan transaksi terakhir.
        """

        if self.riwayat.is_empty():
            print("\nTidak ada transaksi yang dapat dibatalkan.")
            return

        transaksi = self.riwayat.pop()

        if transaksi.jenis == "Peminjaman":

            transaksi.buku.dikembalikan()

            print("\n===== UNDO PEMINJAMAN =====")
            print(f"Peminjaman '{transaksi.buku.judul}' dibatalkan.")
            print(f"Stok sekarang : {transaksi.buku.stok}")

        elif transaksi.jenis == "Pengembalian":

            if transaksi.buku.stok > 0:
                transaksi.buku.dipinjam()

            print("\n===== UNDO PENGEMBALIAN =====")
            print(f"Pengembalian '{transaksi.buku.judul}' dibatalkan.")
            print(f"Stok sekarang : {transaksi.buku.stok}")

        else:

            print("Jenis transaksi tidak dikenali.")