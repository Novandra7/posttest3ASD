class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None
    
    def add_task(self, description):
        task = Task(description)
        if self.head is None:
            self.head = task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = task
    
    def remove_task(self, description):
        current = self.head
        previous = None
        while current is not None:
            if current.description == description:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            else:
                print("<<< to do list yang anda masukkan tidak ada >>>")
                os.system("pause")
            previous = current
            current = current.next
        print("<<< to do list masih kosong >>>")
        return os.system("pause")
    
    def complete_task(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                current.completed = True
                return True
            current = current.next
        print("<<< to do list masih kosong >>>")
        return os.system("pause")
    
    def display_list(self):
        current = self.head
        while current is not None:
            if current.completed:
                print("[x]", current.description)
            else:
                print("[ ]", current.description)
            current = current.next
    
    def mulai(self):
        while True:
            os.system("cls")
            print("1. Tambahkan to do list")
            print("2. Hapus to do list ")
            print("3. Tandai to do list yang kelar")
            print("4. Tampilkan to do list")
            print("5. Quit")
            pilihan = int(input("Masukkan pilihan anda : "))
            if pilihan == 1:
                tdl = input("Masukkan to do list terbaru : ")
                self.add_task(tdl)
            elif pilihan == 2:
                hapus = input("Masukkan to do list yang ingin dihapus : ")
                self.remove_task(hapus)
            elif pilihan == 3:
                tanda = input("Masukkan to do list yang sudah kelar : ")
                self.complete_task(tanda)
            elif pilihan == 4:
                self.display_list()
                os.system("pause")
            else:
                break

            
import os
kaka = ToDoList()
kaka.mulai()

