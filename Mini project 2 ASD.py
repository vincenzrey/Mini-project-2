class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Handphone:
    def __init__(self, kode, nama_merk, model, harga, stok):
        self.kode = kode
        self.nama_merk = nama_merk
        self.model = model
        self.harga = harga
        self.stok = stok

class LinkedList:
    def __init__(self):
        self.head = None
    def kosong(self):
        return self.head is None
    def tambah_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def tambah_akhir(self, data):
        new_node = Node(data)
        if self.kosong():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def tambah_tengah(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
    def hapus_awal(self):
        if self.kosong():
            print("List Kosong")
        else:
            self.head = self.head.next
    def hapus_akhir(self):
        if self.kosong():
            print("List Kosong")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    def hapus_tengah(self, node):
        if self.kosong() or node.next is None:
            print("List Kosong")
        else:
            node.next = node.next.next
    def find_node(self, kode):
        current = self.head
        while current is not None:
            if current.data.kode == kode:
                return current
            current = current.next
        return None
    def create(self):
        kode = int(input("Masukan Kode Hp: "))
        nama_merk = input("Masukan Merk Hp: ")
        model = input("Masukan Nama Hp: ")
        harga = int(input("Masukan Harga Hp: "))
        stok = int(input("Masukan Stok Hp: "))
        print("Pilih 1. Menambah di Awal ")
        print("Pilih 2. Menambah di Akhir ")
        print("Pilih 3. Menambah di Tengah ")
        try:
            pilih = int(input("Masukan Angka: "))
        except ValueError:
            print("Masukan harus angka!")
            return
        if pilih == 1:
            self.tambah_awal(Handphone(kode, nama_merk, model, harga, stok))
        elif pilih == 2:
            self.tambah_akhir(Handphone(kode, nama_merk, model, harga, stok))
        elif pilih == 3:
            kode_setelah = int(input("Masukan kode hp setelah ingin ditambahkan: "))
            node = self.find_node(kode_setelah)
            if node is None:
                print(f"Hp dengan kode {kode_setelah} tidak ditemukan.")
            else:
                self.tambah_tengah(node, Handphone(kode, nama_merk, model, harga, stok))
        else:
            print("Pilihan tidak valid.")
        print(f"Data HP {model} Berhasil Ditambahkan")
    def read(self):
            if self.kosong():
                print("List Kosong")
            else:
                current = self.head
                while current is not None:
                    produk = current.data
                    print("+*********************************************+")
                    print(f"\nKode: {produk.kode}")
                    print(f"Merk: {produk.nama_merk}")
                    print(f"Model: {produk.model}")
                    print(f"Harga: Rp{produk.harga:,}")
                    print(f"Stok: {produk.stok}")
                    print("+*********************************************+")
                    current = current.next
    def update(self):
        kode = int(input("Masukan Kode Hp yang ingin diubah: "))
        node = self.find_node(kode)
        if node is None:
            print(f"Hp dengan kode {kode} tidak ditemukan.")
            return
        new_merk = input("Masukan Merk Hp Baru: ")
        new_model = input("Masukan Nama Hp Baru: ")
        new_harga = int(input("Masukan Harga Hp Baru: "))
        new_stok = int(input("Masukan Stok Hp Baru: "))
        node.data.nama_merk = new_merk
        node.data.model = new_model
        node.data.harga = new_harga
        node.data.stok = new_stok
        print(f"Data Hp dengan kode {kode} berhasil diperbarui.")
    def delete(self):
        print("Pilih cara penghapusan:")
        print("1. Hapus di Awal")
        print("2. Hapus di Akhir")
        print("3. Hapus di Tengah")
        try:
            pilih2 = int(input("Masukkan angka (1/2/3): "))
        except ValueError:
            print("Masukan harus angka!")
            return
        if pilih2 == 1:
            self.hapus_awal()
        elif pilih2 == 2:
            self.hapus_akhir()
        elif pilih2 == 3:
            kode = int(input("Masukan Kode Hp yang ingin dihapus: "))
            node_to_delete = self.find_node(kode)
            if node_to_delete is None:
                print(f"Hp Dengan Kode {kode} Tidak Ditemukan.")
            else:
                self.hapus_tengah(node_to_delete)
                print(f"Hp Dengan Kode {kode} Berhasil Dihapus.")
        else:
            print("Pilihan tidak valid.")

def menu(daftar_handphone):
    while True:
        print("Pilih Menu")
        print("1. Menambah Produk")
        print("2. Melihat Produk")
        print("3. Mengubah Produk")
        print("4. Menghapus Produk")
        print("5. Keluar")
        try:
            pilih = int(input("Silahkan Masukan Angka (1/2/3/4/5) : "))
        except ValueError:
            print("Masukan harus angka!")
            continue
        if pilih == 1:
            daftar_handphone.create()
        elif pilih == 2:
            daftar_handphone.read()
        elif pilih == 3:
            daftar_handphone.update()
        elif pilih == 4:
            daftar_handphone.delete()
        elif pilih == 5:
            break
        else:
            print("Masukan angka 1-5!")

daftar_handphone = LinkedList()
menu(daftar_handphone)



