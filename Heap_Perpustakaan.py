class BinaryHeap:
    """
    Implementasi Binary Heap generik berbasis array (list).

    mode="min" -> Min-Heap (elemen terkecil di puncak/root)
    mode="max" -> Max-Heap (elemen terbesar di puncak/root)

    Setiap elemen heap berupa tuple: (key, data)
        key  -> nilai yang dibandingkan (prioritas / jumlah pinjam)
        data -> dictionary informasi (nama, judul buku, dll)
    """

    def __init__(self, mode="min"):
        self.heap = []
        self.mode = mode 

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _compare(self, a, b):
        """
        Mengembalikan True jika elemen a harus berada
        LEBIH DEKAT ke root dibanding b, sesuai mode heap.
        """
        if self.mode == "min":
            return a[0] < b[0]
        else:
            return a[0] > b[0]

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        """Melihat elemen di puncak heap tanpa menghapusnya. O(1)"""
        if self.is_empty():
            return None
        return self.heap[0]

    def insert(self, key, data):
        """
        Menyisipkan elemen baru ke heap. O(log n)
        Langkah:
          1. Tambahkan elemen baru di posisi paling akhir (leaf terakhir)
          2. "Bubble up" (heapify-up): naikkan elemen selama masih
             melanggar aturan heap terhadap parent-nya
        """
        self.heap.append((key, data))
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        """
        Mengambil sekaligus menghapus elemen di puncak heap. O(log n)
        Langkah:
          1. Simpan elemen root (yang akan dikembalikan)
          2. Pindahkan elemen terakhir ke posisi root
          3. Hapus elemen terakhir (duplikat)
          4. "Bubble down" (heapify-down) dari root agar heap valid lagi
        """
        if self.is_empty():
            return None

        top = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return top

    def build_heap(self, items):
        """
        Membangun heap dari sekumpulan data sekaligus (heapify massal).
        Lebih efisien: O(n) dibanding insert satu-satu O(n log n).
        items: list berisi tuple (key, data)
        """
        self.heap = list(items)
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self._compare(self.heap[i], self.heap[parent]):
                self._swap(i, parent)
                i = parent
            else:
                break

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            target = i 

            if left < n and self._compare(self.heap[left], self.heap[target]):
                target = left
            if right < n and self._compare(self.heap[right], self.heap[target]):
                target = right

            if target != i:
                self._swap(i, target)
                i = target
            else:
                break

    def display_array(self):
        """Menampilkan isi heap sebagai array."""
        if self.is_empty():
            print("   (heap kosong)")
            return
        for idx, (key, data) in enumerate(self.heap):
            label = data.get("label", str(data))
            print(f"   [{idx}] key={key} -> {label}")

    def display_tree(self, i=0, depth=0, prefix="Root: "):
        """Menampilkan heap dalam bentuk struktur pohon (indentasi)."""
        if self.is_empty():
            print("   (heap kosong)")
            return
        if i < len(self.heap):
            key, data = self.heap[i]
            label = data.get("label", str(data))
            print("   " * depth + prefix + f"({key}) {label}")
            if self._left(i) < len(self.heap):
                self.display_tree(self._left(i), depth + 1, "L---> ")
            if self._right(i) < len(self.heap):
                self.display_tree(self._right(i), depth + 1, "R---> ")

KATEGORI_PRIORITAS = {
    "1": ("Dosen", 1),
    "2": ("Mahasiswa Tingkat Akhir", 2),
    "3": ("Mahasiswa", 3),
    "4": ("Anggota Umum", 4),
}

antrian_peminjaman = BinaryHeap(mode="min")
counter_antrian = 0 

def tambah_permintaan_peminjaman():
    global counter_antrian
    print("\n--- TAMBAH PERMINTAAN PEMINJAMAN BUKU ---")
    nama = input("Nama peminjam   : ").strip()
    judul = input("Judul buku      : ").strip()

    print("Kategori anggota:")
    for k, (label, _) in KATEGORI_PRIORITAS.items():
        print(f"   {k}. {label}")
    pilihan = input("Pilih kategori (1-4): ").strip()

    if pilihan not in KATEGORI_PRIORITAS:
        print(">> Kategori tidak valid, permintaan dibatalkan.")
        return

    kategori_label, prioritas = KATEGORI_PRIORITAS[pilihan]
    counter_antrian += 1

    key = (prioritas, counter_antrian)
    data = {
        "nama": nama,
        "judul": judul,
        "kategori": kategori_label,
        "label": f"{nama} | {judul} | Prioritas {prioritas} ({kategori_label})",
    }
    antrian_peminjaman.insert(key, data)
    print(f">> {nama} berhasil masuk antrian dengan prioritas {prioritas} ({kategori_label}).")

def layani_peminjam_berikutnya():
    print("\n--- LAYANI PEMINJAM BERIKUTNYA ---")
    if antrian_peminjaman.is_empty():
        print(">> Antrian kosong, tidak ada yang dilayani.")
        return

    key, data = antrian_peminjaman.extract()
    print(f">> Melayani: {data['nama']} - buku '{data['judul']}' "
          f"({data['kategori']})")

def lihat_antrian():
    print("\n--- DAFTAR ANTRIAN PEMINJAMAN (urutan struktur heap) ---")
    antrian_peminjaman.display_array()
    peek = antrian_peminjaman.peek()
    if peek:
        print(f"\n   >> Berikutnya dilayani: {peek[1]['nama']} ({peek[1]['judul']})")

def lihat_struktur_heap_antrian():
    print("\n--- VISUALISASI STRUKTUR MIN-HEAP ANTRIAN ---")
    antrian_peminjaman.display_tree()

buku_populer = BinaryHeap(mode="max")
data_buku = {}

def _rebuild_heap_populer():
    """Membangun ulang max-heap dari data_buku (dipanggil tiap ada perubahan)."""
    items = []
    for judul, jumlah in data_buku.items():
        items.append((jumlah, {"judul": judul, "label": f"{judul} ({jumlah}x dipinjam)"}))
    buku_populer.build_heap(items)


def tambah_atau_pinjam_buku():
    print("\n--- CATAT PEMINJAMAN BUKU (untuk statistik popularitas) ---")
    judul = input("Judul buku yang dipinjam: ").strip()
    if not judul:
        print(">> Judul tidak boleh kosong.")
        return

    data_buku[judul] = data_buku.get(judul, 0) + 1
    _rebuild_heap_populer()
    print(f">> Buku '{judul}' sekarang telah dipinjam {data_buku[judul]}x.")


def lihat_top_n_buku():
    print("\n--- TOP BUKU TERPOPULER ---")
    if buku_populer.is_empty():
        print(">> Belum ada data peminjaman buku.")
        return

    try:
        n = int(input("Tampilkan berapa buku teratas? "))
    except ValueError:
        n = 5

    temp = BinaryHeap(mode="max")
    temp.build_heap(list(buku_populer.heap))

    print(f"\n   TOP {n} BUKU TERPOPULER:")
    rank = 1
    while not temp.is_empty() and rank <= n:
        key, data = temp.extract()
        print(f"   {rank}. {data['judul']} - dipinjam {key}x")
        rank += 1


def lihat_struktur_heap_populer():
    print("\n--- VISUALISASI STRUKTUR MAX-HEAP BUKU TERPOPULER ---")
    buku_populer.display_tree()
