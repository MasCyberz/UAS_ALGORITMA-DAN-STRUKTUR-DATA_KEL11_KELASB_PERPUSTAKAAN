class BinaryHeap:
    """
    Binary Heap generik untuk menyimpan data buku berdasarkan prioritas.

    mode = "min" -> Min Heap (nilai key paling kecil jadi root)
    mode = "max" -> Max Heap (nilai key paling besar jadi root)

    Setiap elemen disimpan dalam bentuk tuple:
        (key, value)

    key   : angka yang dipakai untuk menentukan prioritas
            (misal: rating, jumlah pinjam, atau stok)
    value : data buku itu sendiri (bisa dict, object, dll) 
    """

    def __init__(self, mode="min"):
        # Tempat menyimpan seluruh elemen heap dalam bentuk list/array
        self.heap = []
        # Menentukan apakah ini min-heap atau max-heap
        self.mode = mode.lower()

    def _parent(self, index):
        """
        Mencari index parent dari suatu node.
        Rumus standar heap berbasis array.
        """
        return (index - 1) // 2

    def _left(self, index):
        """
        Mencari index anak kiri dari suatu node.
        """
        return 2 * index + 1

    def _right(self, index):
        """
        Mencari index anak kanan dari suatu node.
        """
        return 2 * index + 2

    def _compare(self, a, b):
        """
        Membandingkan dua elemen (a dan b), masing-masing berbentuk (key, value).
        Mengembalikan True apabila 'a' harus berada
        lebih dekat ke root dibanding 'b'.
        - Kalau mode "min": key lebih kecil menang (naik ke atas)
        - Kalau mode "max": key lebih besar menang (naik ke atas)
        """
        if self.mode == "min":
            return a[0] < b[0]
        return a[0] > b[0]

    def _swap(self, i, j):
        """
        Menukar posisi dua elemen di array heap.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        """
        Lihat elemen root tanpa menghapusnya.
        """
        if self.is_empty():
            return None

        return self.heap[0]

    def insert(self, key, value):
        """
        Menambah elemen baru: taruh di akhir, lalu naikkan ke posisi yang benar.
        """
        self.heap.append((key, value))

        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        """
        Mengambil & menghapus root: gantikan dengan elemen terakhir, lalu turunkan.
        """
        if self.is_empty():
            return None

        root = self.heap[0]

        last = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        """
        Menaikkan elemen selama masih lebih diprioritaskan dari parent-nya.
        """
        while index > 0:

            parent = self._parent(index) 
            if self._compare(self.heap[index], self.heap[parent]):
                self._swap(index, parent)
                index = parent

            else:
                break

    def _heapify_down(self, index):
        """
        Menurunkan elemen selama masih ada anak yang lebih diprioritaskan.
        """
        size = len(self.heap)
        while True:

            left = self._left(index)
            right = self._right(index)
            target = index

            if left < size and self._compare(self.heap[left], self.heap[target]):
                target = left

            if right < size and self._compare(self.heap[right], self.heap[target]):
                target = right

            if target == index:
                break
                
            self._swap(index, target)
            index = target

    def build_heap(self, data):
        """
        Membangun heap dari list yang sudah ada tanpa insert satu-satu (O(n)).
        """
        self.heap = list(data) 
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def display(self):
        """
        Menampilkan isi heap apa adanya (bukan urutan prioritas).
        """
        if self.is_empty():
            print("Heap kosong.")
            return

        print("\nIsi Heap\n")

        for i, (key, value) in enumerate(self.heap):
            print(f"{i}. Key = {key} | Value = {value}")

    def display_tree(self, index=0, ident="", branch="Root"):
        """
        Menampilkan heap dalam bentuk pohon.
        """
        if self.is_empty():
            print("Heap kosong.")
            return

        if index >= len(self.heap):
            return

        priority, data = self.heap[index]
        anggota = data["anggota"]

        indent = "   " * ident

        print(
            f"{indent}{branch} "
            f"[Prioritas: {priority}] "
            f"{anggota.nama} "
            f"({anggota.kategori}) "
            f"=> Buku {data['id_buku']}"
        )

        # print(
        #     "   " * level +
        #     prefix +
        #     f"{key} : {value}"
        # )

        # self.display_tree(self._left(index), level + 1, "L---- ") 
        # self.display_tree(self._right(index), level + 1, "R---- ")

        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap):
            self.display_tree(left, indent + "│   ", "├──L")

        if right < len(self.heap):
            self.display_tree(right, indent + "│   ", "└──R")
