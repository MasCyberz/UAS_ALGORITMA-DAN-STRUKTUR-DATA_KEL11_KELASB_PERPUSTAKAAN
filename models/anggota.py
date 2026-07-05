class Anggota:
    """
    Model data anggota perpustakaan.
    """

    def __init__(self, nim, nama, kategori):
        self.nim = nim
        self.nama = nama
        self.kategori = kategori

    def __str__(self):
        return (
            f"{self.nim} - "
            f"{self.nama} "
            f"({self.kategori})"
        )