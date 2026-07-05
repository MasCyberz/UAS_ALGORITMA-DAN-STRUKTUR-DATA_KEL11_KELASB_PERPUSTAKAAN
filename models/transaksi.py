class Transaksi:
    """
    Menyimpan informasi transaksi
    peminjaman atau pengembalian buku.
    """

    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku

    def __str__(self):
        return (
            f"{self.anggota.nama} "
            f"meminjam "
            f"'{self.buku.judul}'"
        )