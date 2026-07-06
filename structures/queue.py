class Queue:
    
    """
    Queue (FIFO) diimplementasikan menggunakan list Python.
    - enqueue -> list.append()  (menambah di belakang antrian)
    - dequeue -> list.pop(0)    (mengambil dari depan antrian)
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        """
        Menambahkan data ke belakang antrian.
        """
        self.items.append(data)

    def dequeue(self):
        """
        Mengeluarkan dan mengembalikan data paling depan antrian.
        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """
        Melihat data paling depan tanpa mengeluarkannya.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
            return
        print("\nIsi Antrian (depan -> belakang)\n")
        for idx, data in enumerate(self.items):
            print(f"{idx}. {data}")
