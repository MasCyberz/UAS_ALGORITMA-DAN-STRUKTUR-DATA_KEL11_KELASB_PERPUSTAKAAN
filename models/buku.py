class Buku:
    """
    Model data buku.
    Digunakan oleh BST sebagai data utama yang disimpan.
    """

    def __init__(self, id_buku: str, judul, penulis, tahun, stok):
        self.id = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.stok = stok

    def dipinjam(self):
        """
        Mengurangi stok buku jika masih tersedia.
        """
        if self.stok > 0:
            self.stok -= 1
            return True
        return False

    def dikembalikan(self):
        """
        Menambah stok buku.
        """
        self.stok += 1

    def __str__(self):
        return (
            f"[{self.id}] "
            f"{self.judul} - "
            f"{self.penulis} "
            f"({self.tahun}) | "
            f"Stok: {self.stok}"
        )