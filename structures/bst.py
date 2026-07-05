from structures.queue import Queue


class Node:
    """
    Node = satu “kotak” di dalam pohon BST.

    Di sini kita menyimpan:
    - data buku
    - anak kiri (left)
    - anak kanan (right)
    """

    def __init__(self, buku):
        # Menyimpan objek buku di dalam node
        self.data = buku

        # Awalnya belum punya anak
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) untuk menyimpan data buku.

    Cara kerja BST:
    - Buku dengan ID lebih kecil → ke kiri
    - Buku dengan ID lebih besar → ke kanan
    - ID tidak boleh sama (harus unik)
    """

    def __init__(self):
        # Root = node paling atas (awal pohon)
        self.root = None

    # INSERT DATA BUKU

    def insert(self, buku):
        """
        Menambahkan buku ke dalam BST.
        """

        # Jika pohon masih kosong, langsung jadi root
        if self.root is None:
            self.root = Node(buku)
            return True

        # Kalau sudah ada isi, cari posisi yang tepat
        return self._insert(self.root, buku)

    def _insert(self, current, buku):
        """
        Proses pencarian posisi insert (rekursif).
        """

        # Kalau ID lebih kecil, masuk ke kiri
        if buku.id < current.data.id:

            # Kalau kiri kosong, taruh di sini
            if current.left is None:
                current.left = Node(buku)
                return True

            # Kalau belum kosong, lanjut ke subtree kiri
            return self._insert(current.left, buku)

        # Kalau ID lebih besar, masuk ke kanan
        elif buku.id > current.data.id:

            # Kalau kanan kosong, taruh di sini
            if current.right is None:
                current.right = Node(buku)
                return True

            # Kalau belum kosong, lanjut ke subtree kanan
            return self._insert(current.right, buku)

        else:
            # Kalau ID sama, data ditolak (tidak boleh duplikat)
            return False

    # SEARCH DATA BUKU

    def search(self, id_buku):
        """
        Mencari buku berdasarkan ID.
        """
        return self._search(self.root, id_buku)

    def _search(self, current, id_buku):
        """
        Proses pencarian secara rekursif.
        """

        # Kalau sudah mentok (tidak ketemu)
        if current is None:
            return None

        # Kalau ketemu ID yang sama
        if id_buku == current.data.id:
            return current.data

        # Kalau lebih kecil, cari ke kiri
        if id_buku < current.data.id:
            return self._search(current.left, id_buku)

        # Kalau lebih besar, cari ke kanan
        return self._search(current.right, id_buku)

    # DELETE NODE

    def delete(self, id_buku):
        """
        Menghapus node berdasarkan id_buku.
        """

        self.root = self._delete(self.root, id_buku)


    def _delete(self, current, id_buku):

        if current is None:
            return None

        # cari ke kiri
        if id_buku < current.data.id:
            current.left = self._delete(current.left, id_buku)

        # cari ke kanan
        elif id_buku > current.data.id:
            current.right = self._delete(current.right, id_buku)

        # ketemu node yang mau dihapus
        else:

            # CASE 1: tidak punya anak
            if current.left is None and current.right is None:
                return None

            # CASE 2: hanya punya 1 anak (kanan)
            if current.left is None:
                return current.right

            # CASE 2: hanya punya 1 anak (kiri)
            if current.right is None:
                return current.left

            # CASE 3: punya 2 anak
            successor = self._find_min(current.right)
            current.data = successor.data
            current.right = self._delete(current.right, successor.data.id)

        return current

    # INORDER TRAVERSAL

    def inorder(self):
        """
        Menampilkan semua buku secara urut berdasarkan ID.

        Urutan Inorder:
        Kiri → Akar → Kanan
        """

        hasil = []
        self._inorder(self.root, hasil)
        return hasil

    def _inorder(self, current, hasil):
        """
        Versi rekursif untuk mengumpulkan data.
        """

        if current is None:
            return

        # Kunjungi kiri dulu
        self._inorder(current.left, hasil)

        # Simpan data node sekarang
        hasil.append(current.data)

        # Kunjungi kanan
        self._inorder(current.right, hasil)

    # LEVEL ORDER (BFS)

    def level_order(self):
        """
        Menampilkan data berdasarkan level (BFS).

        Artinya:
        - Root dulu
        - Lalu anak-anaknya
        - Lalu level berikutnya
        """

        hasil = []

        if self.root is None:
            return hasil

        # Gunakan queue untuk BFS
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():

            # Ambil data paling depan
            current = queue.dequeue()

            hasil.append(current.data)

            # Masukkan anak kiri ke queue
            if current.left is not None:
                queue.enqueue(current.left)

            # Masukkan anak kanan ke queue
            if current.right is not None:
                queue.enqueue(current.right)

        return hasil

    # TAMPILKAN STRUKTUR POHON

    def display(self):
        """
        Menampilkan struktur pohon BST agar mudah dibaca.
        """

        if self.root is None:
            print("BST kosong.")
            return

        self._display(self.root)

    def _display(self, current, level=0, prefix="Root : "):
        """
        Menampilkan pohon dengan format bercabang.
        """

        if current is None:
            return

        # Tampilkan node saat ini
        print(
            "   " * level +
            prefix +
            f"[{current.data.id}] {current.data.judul}"
        )

        # Rekursi ke kiri
        self._display(current.left, level + 1, "L---- ")

        # Rekursi ke kanan
        self._display(current.right, level + 1, "R---- ")

    # TINGGI POHON

    def height(self):
        """
        Menghitung tinggi pohon BST.
        (Seberapa dalam pohonnya)
        """
        return self._height(self.root)

    def _height(self, current):
        """
        Rekursi untuk mencari tinggi pohon.
        """

        # Kalau node kosong
        if current is None:
            return -1  # pohon kosong

        # Hitung tinggi kiri dan kanan
        left_height = self._height(current.left)
        right_height = self._height(current.right)

        # Ambil yang paling tinggi + 1 (node sekarang)
        return 1 + max(left_height, right_height)

    # JUMLAH NODE

    def count_nodes(self):
        """
        Menghitung total semua node (buku) dalam BST.
        """
        return self._count_nodes(self.root)

    def _count_nodes(self, current):
        """
        Rekursi untuk menghitung jumlah node.
        """

        if current is None:
            return 0

        # 1 untuk node sekarang + kiri + kanan
        return (
            1 +
            self._count_nodes(current.left) +
            self._count_nodes(current.right)
        )