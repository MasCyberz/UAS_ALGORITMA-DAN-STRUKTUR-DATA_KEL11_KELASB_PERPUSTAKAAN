# Sistem Manajemen Perpustakaan – UAS Algoritma dan Struktur Data

Untuk proyek UAS mata kuliah Algoritma dan Struktur Data, kelompok kami memilih studi kasus **perpustakaan**. Proyek ini adalah implementasi sistem perpustakaan sederhana berbasis **Command Line Interface (CLI)** yang mengintegrasikan empat struktur data fundamental:
- **Queue** – Antrian peminjaman
- **Stack** – Riwayat transaksi & undo
- **Binary Search Tree (BST)** – Katalog buku
- **Binary Heap** – Prioritas peminjaman

Seluruh struktur data dibangun dari nol menggunakan Python dan saling terhubung dalam satu alur bisnis perpustakaan yang nyata.

---

## Anggota Kelompok

| No | Nama | NIM | Username Github | 
|----|------|-----| ----------------|
| 1  | Dimas Alif Ardiansyah | K3525004 | MasCyberz |
| 2  | Jihan Sofia Kamila | K3525029 | seopheea |
| 3  | Vincensius Vicko Riska Saputra | K3525042 | pikoopikk |

---

## Fitur Utama

| Kode | Fitur | Struktur Data |
|------|-------|---------------|
| 1 | Tambah buku baru | BST |
| 2 | Tampilkan seluruh buku (terurut ID) | BST (Inorder) |
| 3 | Cari buku berdasarkan ID | BST (Search) |
| 4 | Hapus buku | BST (Delete) |
| 5 | Info katalog: jumlah buku, tinggi pohon, level-order | BST (Height, Count, BFS) |
| 6 | Ajukan peminjaman (masuk antrian) | Queue |
| 7 | Tampilkan antrian peminjaman | Queue |
| 8 | Proses antrian → prioritas (berdasarkan kategori anggota) | Queue → Heap |
| 9 | Lihat heap prioritas dalam bentuk pohon | Min Heap |
| 10 | Proses peminjaman dari heap | Heap → BST (kurangi stok) → Stack (catat transaksi) |
| 11 | Kembalikan buku | BST (tambah stok) → Stack (catat transaksi) |
| 12 | Lihat riwayat transaksi (atas ke bawah) | Stack |
| 13 | Undo transaksi terakhir | Stack (pop) + rollback stok di BST |

---

## Struktur Data yang Diimplementasikan

### 1. Queue (FIFO)
- **Lokasi:** `structures/queue.py`
- **Digunakan untuk:** Antrian peminjaman. Anggota yang mengajukan pinjam masuk ke dalam queue secara berurutan.
- **Operasi:** `enqueue()`, `dequeue()`, `is_empty()`, `peek()`

### 2. Stack (LIFO)
- **Lokasi:** `structures/stack.py`
- **Digunakan untuk:** Menyimpan riwayat transaksi (peminjaman & pengembalian). Transaksi terbaru berada di puncak stack, memungkinkan fitur **undo**.
- **Operasi:** `push()`, `pop()`, `peek()`, `is_empty()`

### 3. Binary Search Tree (BST)
- **Lokasi:** `structures/bst.py`
- **Digunakan untuk:** Katalog buku. Buku disimpan dalam node BST dengan key = ID buku.
- **Operasi:** `insert()`, `search()`, `delete()`, `inorder()`, `level_order()`, `height()`, `count_nodes()`
- **Aturan:** ID lebih kecil ke kiri, ID lebih besar ke kanan, ID duplikat ditolak.

### 4. Binary Heap (Min Heap)
- **Lokasi:** `structures/binary_heap.py`
- **Digunakan untuk:** Menentukan prioritas peminjaman berdasarkan kategori anggota.
  - Dosen → prioritas 1 (tertinggi)
  - Staff → prioritas 2
  - Mahasiswa Tingkat Akhir → prioritas 3
  - Mahasiswa → prioritas 4
  - Lainnya → prioritas 5
- **Operasi:** `insert()`, `extract()`, `build_heap()`, `peek()`, `is_empty()`, serta `display_tree()` untuk visualisasi heap.

---

## Integrasi Antar Struktur Data

Alur bisnis perpustakaan menghubungkan keempat struktur data sebagai berikut:

```
Anggota mengajukan pinjam
        │
        ▼
    [ Queue ]
        │  (proses antrian ke prioritas)
        ▼
    [ Min Heap ]   ← prioritas berdasarkan kategori
        │
        │  (proses peminjaman berikutnya)
        ▼
    [ BST ]        ← periksa & kurangi stok buku
        │
        ▼
    [ Stack ]      ← catat transaksi peminjaman

Pengembalian buku:
    [ BST ]        ← tambah stok
        │
        ▼
    [ Stack ]      ← catat transaksi pengembalian

Undo transaksi:
    [ Stack ]      ← pop transaksi terakhir
        │
        ▼
    [ BST ]        ← rollback stok buku
```

Dengan integrasi ini, setiap transaksi selalu menjaga konsistensi data di seluruh struktur.

---

## Struktur Proyek

```
.
├── main.py                           # Entry point program, menu CLI
├── services/
│   └── perpustakaan_services.py      # Logika bisnis & integrasi struktur data
├── models/
│   ├── buku.py                       # Kelas Buku
│   ├── anggota.py                    # Kelas Anggota
│   └── transaksi.py                  # Kelas Transaksi
├── structures/
│   ├── bst.py                        # Implementasi Binary Search Tree
│   ├── queue.py                      # Implementasi Queue (FIFO)
│   ├── stack.py                      # Implementasi Stack (LIFO)
│   └── binary_heap.py                # Implementasi Binary Heap (Min/Max)
└── README.md                         # Dokumentasi ini
```

---

## Cara Menjalankan

1. Pastikan Python 3.7+ terinstal.
2. Clone atau salin seluruh folder proyek.
3. Buka terminal di root folder proyek.
4. Jalankan perintah:
   ```bash
   python main.py
   ```
5. Ikuti petunjuk menu yang muncul di layar.

**Catatan:** Program ini tidak memerlukan library eksternal, murni menggunakan modul bawaan Python.

---

## Contoh Penggunaan

1. **Tambah buku** → masukkan ID, judul, penulis, tahun, stok.
2. **Tampilkan katalog** → semua buku muncul terurut berdasarkan ID.
3. **Ajukan peminjaman** → masukkan NIM anggota (jika baru akan didaftarkan), lalu ID buku. Anggota masuk ke antrian.
4. **Proses antrian ke prioritas** → memindahkan satu data dari antrian ke heap prioritas.
5. **Proses peminjaman berikutnya** → mengambil data teratas heap, mengurangi stok buku di BST, dan menyimpan transaksi di stack.
6. **Kembalikan buku** → masukkan NIM dan ID buku, stok bertambah, transaksi tercatat.
7. **Undo transaksi** → membatalkan transaksi terakhir (peminjaman atau pengembalian) dengan mengembalikan stok semula.

---

## Kesimpulan

Proyek ini berhasil membangun sebuah sistem manajemen perpustakaan yang memadukan empat struktur data inti—Queue, Stack, BST, dan Binary Heap—dalam satu kesatuan yang koheren. 

- **Queue** menjaga keadilan urutan pengajuan peminjaman,  
- **Heap** memberikan prioritas berbasis kategori anggota secara efisien,  
- **BST** menyediakan akses cepat dan terurut untuk data buku, serta  
- **Stack** memungkinkan pencatatan riwayat transaksi dan fitur undo yang sederhana namun andal.  

Melalui proyek ini, kami tidak hanya mengimplementasikan masing-masing struktur data secara mandiri, tetapi juga mendemonstrasikan bagaimana mereka dapat diintegrasikan untuk menyelesaikan permasalahan nyata secara harmonis. Setiap operasi bisnis (peminjaman, pengembalian, pembatalan) menjaga konsistensi data di seluruh struktur, menunjukkan pemahaman mendalam tentang karakteristik dan kegunaan setiap struktur data dalam konteks aplikatif.

---

**Universitas Sebelas Maret**  
**Mata Kuliah: Algoritma dan Struktur Data**  
**Kelas B / Semester 2**