class BinaryHeap:
    """
    Binary Heap generik.

    mode = "min" -> Min Heap
    mode = "max" -> Max Heap

    Setiap elemen disimpan dalam bentuk tuple:
        (key, value)

    key   : nilai yang dibandingkan
    value : objek/data yang disimpan

    key  -> nilai yang dibandingkan (prioritas / jumlah pinjam)
    data -> dictionary informasi (nama, judul buku, dll)
    """

    def __init__(self, mode="min"):
        self.heap = []
        self.mode = mode.lower()

    # Helper Index

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    # Helper Compare

    def _compare(self, a, b):
        """
        Mengembalikan True apabila a memiliki prioritas
        lebih tinggi daripada b.
        """

        if self.mode == "min":
            return a[0] < b[0]

        return a[0] > b[0]

    # Helper Swap

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Informasi Heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        """
        Mengambil elemen root
        tanpa menghapusnya.
        """

        if self.is_empty():
            return None

        return self.heap[0]

    # Insert

    def insert(self, key, value):
        """
        Menambahkan data baru ke heap.
        """

        self.heap.append((key, value))
        self._heapify_up(len(self.heap) - 1)

    # Extract Root

    def extract(self):
        """
        Mengambil root heap.
        """

        if self.is_empty():
            return None

        root = self.heap[0]

        last = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last
            self._heapify_down(0)

        return root

    # Heapify Up

    def _heapify_up(self, index):

        while index > 0:

            parent = self._parent(index)

            if self._compare(
                self.heap[index],
                self.heap[parent]
            ):

                self._swap(index, parent)
                index = parent

            else:
                break

    # Heapify Down

    def _heapify_down(self, index):

        size = len(self.heap)

        while True:

            left = self._left(index)
            right = self._right(index)

            target = index

            if (
                left < size and
                self._compare(
                    self.heap[left],
                    self.heap[target]
                )
            ):
                target = left

            if (
                right < size and
                self._compare(
                    self.heap[right],
                    self.heap[target]
                )
            ):
                target = right

            if target == index:
                break

            self._swap(index, target)
            index = target

    # Build Heap

    def build_heap(self, data):
        """
        Membangun heap dari list.
        """

        self.heap = list(data)

        for i in range(
            len(self.heap) // 2 - 1,
            -1,
            -1
        ):
            self._heapify_down(i)

    # Display

    def display(self):

        if self.is_empty():

            print("Heap kosong.")
            return

        print("\nIsi Heap\n")

        for i, (key, value) in enumerate(self.heap):
            print(f"{i}. Key = {key} | Value = {value}")

    # Display Tree

    def display_tree(
        self,
        index=0,
        level=0,
        prefix="Root : "
    ):

        if self.is_empty():
            print("Heap kosong.")
            return

        if index >= len(self.heap):
            return

        key, value = self.heap[index]

        print(
            "   " * level +
            prefix +
            f"{key} : {value}"
        )

        self.display_tree(
            self._left(index),
            level + 1,
            "L---- "
        )

        self.display_tree(
            self._right(index),
            level + 1,
            "R---- "
        )