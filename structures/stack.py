class Stack:
    
    """
    Stack (LIFO) diimplementasikan menggunakan list Python.
    - push  -> list.append()  (menambah di ujung/akhir list)
    - pop   -> list.pop()     (mengambil dari ujung/akhir list)
    Ujung list (index terakhir) dianggap sebagai "puncak" stack.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, data):
        """
        Menambahkan data ke puncak stack.
        """
        self.items.append(data)

    def pop(self):
        """
        Mengeluarkan dan mengembalikan data di puncak stack.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Melihat data di puncak tanpa mengeluarkannya.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def display(self):
        if self.is_empty():
            print("Stack kosong.")
            return
        print("\nIsi Stack (atas -> bawah)\n")
        for idx, data in enumerate(reversed(self.items), start=1 ):
            print(f"{idx}. {data}")
