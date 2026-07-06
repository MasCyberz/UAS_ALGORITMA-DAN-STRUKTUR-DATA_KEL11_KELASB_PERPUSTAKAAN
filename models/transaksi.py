class Transaksi:
    """
    Menyimpan informasi transaksi
    peminjaman atau pengembalian buku.
    """

    def __init__(self, anggota, buku, jenis):
        self.anggota = anggota
        self.buku = buku
        self.jenis = jenis

    def __str__(self):
        return (
            f"{self.jenis} | "
            f"{self.anggota.nama} | "
            f"{self.buku.judul}"
        )