from sistem import *
from config import *
from datetime import datetime

def admin_login():
    """Admin login"""
    clear_screen()
    print("=" * 50)
    print("Login Admin - Gie's Library")
    print("=" * 50)
    
    username = input("\nUsername: ").strip()
    password = input("Password: ").strip()
    
    if username == ADMIN_USN and password == ADMIN_PW:
        print("\n Login berhasil! Selamat datang, Admin!")
        pause()
        return True
    else:
        print("\n✗ Username atau password salah!")
        pause()
        return False

# def display_items(items, item_type):
#     """Generic display function"""
#     if not items:
#         print(f"\nBelum ada data {item_type}.")
#         return False
    
#     for idx, item in enumerate(items, 1):
#         if item_type == "buku":
#             print(f"{idx:<2}. {item['id_buku']:<10} | {item['kategori']:<20} | {item['judul_buku']:<20} | {item['nama_penulis']:<20} | {item['stok']:<5} | {item['tgl']:<12}")
#         elif item_type == "user":
#             print(f"{idx:<2}. {item['id_user']:<10} | {item['nama']:<20} | {item['umur']:<5} | {item['no_telp']:<15} | {item['member']:<10}")
#     return True
    
def display_items(items, item_type):
    if not items:
        print(f"\nBelum ada data {item_type}.")
        return False
    
    for idx, item in enumerate(items, 1):
        if isinstance(item, str):
            item = eval(item)

        if item_type == "buku":
            print(f"{idx:<2}. {item['id_buku']:<10} | {item['kategori']:<20} | {item['judul_buku']:<20} | {item['nama_penulis']:<20} | {item['stok']:<5} | {item['tgl']:<12}")
        
        elif item_type == "user":
            print(f"{idx:<2}. {item['id_user']:<10} | {item['nama']:<20} | {item['umur']:<5} | {item['no_telp']:<15} | {item['member']:<10}")
    
    return True
    
def tampil_data(file, item_type):
    """Generic view function with sorting option"""
    clear_screen()
    print("=" * 50)
    print(f"Dashboard Admin - Tampil Data {item_type}")
    print("=" * 50)
    
    data = baca_data(file)
    
    if data:
        if item_type == "buku":
            print("\nUrutan tampilan:")
            print("1. Alphabetical (A-Z)")
            print("2. Data terbaru")
            sort_choice = input("\nPilih urutan (1): ").strip()
            
            if sort_choice == "1":
                if item_type == "buku":
                    data = sorted(data, key=lambda x: x['id_buku'])
            elif sort_choice == "2":
                data = sorted(data, key=lambda x: datetime.strptime(x['tgl'], "%d-%m-%Y"), reverse=True)
            else:
                print("Input tidak sesuai")
        elif item_type == "user":
            print("\nUrutan tampilan:")
            print("1. Alphabetical (A-Z)")
            sort_choice = input("\nPilih urutan (1): ").strip()
            
            if sort_choice == "1":
                data = sorted(data, key=lambda x: x['nama'])
            else:
                print("Input tidak sesuai")
                
    if item_type == "buku":
        print(f"No. {'Kode Buku':<10} | {'Kategori':<20} | {'Judul Buku':<20} | {'Nama Penulis':<20} | {'Stok':<5} | {'Tanggal':<12}") 
    elif item_type == "user":
        print(f"No. {'ID User':<10} | {'Nama':<20} | {'Umur':<5} | {'No. Telp':<15} | {'Member':<10}") 
    display_items(data, item_type)
    pause()

def tambah_data(file, item_type):
    """Generic add function"""
    clear_screen()
    print("=" * 50)
    print(f"Dashboard Admin - Tambah Data {item_type}")
    print("=" * 50)
    
    data = baca_data(file)
    
    if item_type == "buku":
        id_buku = input("\nKode Buku: ").strip().upper()
        kategori = input("Kategori: ").strip()
        judul_buku = input("Judul Buku: ").strip()
        nama_penulis = input("Nama Penulis: ").strip()
        stok = input("Stok: ").strip()
        tgl = datetime.now().strftime("%d-%m-%Y")
        
        if any(item['id_buku'] == id_buku for item in data):
            print("\nKode Buku sudah ada! Gunakan kode lain.")
            pause()
            return
        
        new_item = {
            "id_buku": id_buku,
            "kategori": kategori,
            "judul_buku": judul_buku,
            "nama_penulis": nama_penulis,
            "stok": stok,
            "tgl": tgl
        }
        
    elif item_type == "user":
        id_user = input("\nID User: ").strip().upper()
        nama = input("Nama: ").strip()
        umur = input("Umur: ").strip()
        no_telp = input("No. Telp: ").strip()
        member = input("Member (ada/tidak ada): ").strip()
        
        if any(item['id_user'] == id_user for item in data):
            print("\nID User sudah ada! Gunakan ID lain.")
            pause()
            return
        
        new_item = {
            "id_user": id_user,
            "nama": nama,
            "umur": umur,
            "no_telp": no_telp,
            "member": member
        }
    
    else:
        print("\nTipe data tidak dikenali!")
        pause()
        return
    
    data.append(new_item)
    simpan_data(file, data)
    print("\n✓ Data berhasil ditambahkan!")
    pause()

def edit_data(file, item_type):
    """Generic edit function"""
    clear_screen()
    print("=" * 50)
    print(f"Dashboard Admin - Edit Data {item_type}")
    print("=" * 50)
    
    data = baca_data(file)
    
    if not display_items(data, item_type):
        pause()
        return
    
    try:
        idx = int(input("\nPilih nomor data yang ingin diedit: ").strip())
        if idx < 1 or idx > len(data):
            raise ValueError
    except ValueError:
        print("\nInput tidak valid!")
        pause()
        return
    
    item = data[idx - 1]
    
    if item_type == "buku":
        print("\nKosongkan input untuk mempertahankan nilai lama.")
        kategori = input(f"Kategori ({item['kategori']}): ").strip() or item['kategori']
        judul_buku = input(f"Judul Buku ({item['judul_buku']}): ").strip() or item['judul_buku']
        nama_penulis = input(f"Nama Penulis ({item['nama_penulis']}): ").strip() or item['nama_penulis']
        stok = input(f"Stok ({item['stok']}): ").strip() or item['stok']
        
        # Update data
        item.update({
            "kategori": kategori,
            "judul_buku": judul_buku,
            "nama_penulis": nama_penulis,
            "stok": stok,
            "tgl": datetime.now().strftime("%d-%m-%Y") 
        })
    elif item_type == "user":
        print("\nKosongkan input untuk mempertahankan nilai lama.")
        nama = input(f"Nama ({item['nama']}): ").strip() or item['nama']
        umur = input(f"Umur ({item['umur']}): ").strip() or item['umur']
        no_telp = input(f"No. Telp ({item['no_telp']}): ").strip() or item['no_telp']
        member = input(f"Member ({item['member']}): ").strip() or item['member']
        
        # Update data
        item.update({
            "nama": nama,
            "umur": umur,
            "no_telp": no_telp,
            "member": member
        })
        
    simpan_data(file, data)
    print("\nData berhasil diperbarui!")
    pause()

def hapus_data(file, item_type):   
    """Generic delete function"""
    clear_screen()
    print("=" * 50)
    print(f"Dashboard Admin - Hapus Data {item_type}")
    print("=" * 50)
    
    data = baca_data(file)
    
    if not display_items(data, item_type):
        pause()
        return
    
    try:
        idx = int(input("\nPilih nomor data yang ingin dihapus: ").strip())
        if idx < 1 or idx > len(data):
            raise ValueError
    except ValueError:
        print("\nInput tidak valid!")
        pause()
        return
    
    confirm = input("\nApakah Anda yakin ingin menghapus data ini? (y/n): ").strip().lower()
    if confirm == 'y':
        del data[idx - 1]
        simpan_data(file, data)
        print("\nData berhasil dihapus!")
    else:
        print("\nPenghapusan dibatalkan.")
    
    pause()

def crud_menu(file, item_type):
    """Generic CRUD menu"""
    while True:
        clear_screen()
        print("=" * 50)
        print(f"Dashboard Admin - Data {item_type}")
        print("=" * 50)
        print("1. Tampilkan Daftar")
        print("2. Tambah Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("0. Kembali")
        
        choice = input("\nPilih (0-4): ").strip()
        
        if choice == "1":
            tampil_data(file, item_type)
        elif choice == "2":
            tambah_data(file, item_type)
        elif choice == "3":
            edit_data(file, item_type)
        elif choice == "4":
            hapus_data(file, item_type)
        elif choice == "0":
            break

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def tampilkan(self):
        current = self.head
        if not current:
            print("Belum ada data peminjaman.")
            return
        
        no = 1
        while current:
            print(f"{no}. {current.data}")
            current = current.next
            no += 1

def proses_peminjaman(ll_peminjaman):
    data_buku = baca_data(BUKU_FILE)
    display_items(data_buku, "buku")

    id_user = input("\nMasukkan ID User: ")

    # cek member
    if not cek_member(id_user):
        print("❌ User bukan member! Harus daftar dulu.")
        input("Tekan ENTER untuk lanjut...")
        return

    print("✅ Member ditemukan.")

    input_buku = input("Masukkan ID / Judul Buku: ")
    buku = cari_buku(input_buku, data_buku)

    if not buku:
        print("❌ Buku tidak ditemukan.")
        return

    if int(buku["stok"]) <= 0:
        print("❌ Stok buku habis.")
        return

    konfirmasi = input("Izinkan peminjaman? (y/n): ")
    if konfirmasi.lower() == 'y':

        data_pinjam = {
            "id_user": id_user,
            "id_buku": buku["id_buku"],
            "judul_buku": buku["judul_buku"],
            "tgl_peminjaman": datetime.now().strftime("%d-%m-%Y")
        }

        ll_peminjaman.tambah(data_pinjam)
        buku["stok"] = int(buku["stok"]) - 1

        simpan_data(BUKU_FILE, data_buku)

        print("✅ Buku berhasil dipinjam!")
        pause()
    else:
        print("❌ Peminjaman dibatalkan.")
        pause()

def peminjaman_menu(ll_peminjaman):
    """Menu peminjaman buku"""
    while True:
        clear_screen()
        print("=" * 50)
        print("Dashboard Admin - Peminjaman Buku")
        print("=" * 50)
        print("1. Proses Peminjaman")
        print("2. Tampilkan Data Peminjaman")
        print("0. Kembali")
        
        choice = input("\nPilih (0-2): ").strip()
        
        if choice == "1":
            proses_peminjaman(ll_peminjaman)
        elif choice == "2":
            ll_peminjaman.tampilkan()
            pause()
        elif choice == "0":
            break


def admin_menu():
    """Admin main menu"""
    ll_peminjaman = LinkedList()
    while True:
        clear_screen()
        print("=" * 50)
        print("Dashboard Admin - Gie's Library")
        print("=" * 50)
        print("1. Kelola Data Buku")
        print("2. Kelola Data Pengunjung")
        print("3. Kelola Data Peminjaman")
        # print("4. Cetak Laporan")
        print("0. Logout")
        
        choice = input("\nPilih (0-2): ").strip()
        
        if choice == "1":
            crud_menu(BUKU_FILE, "buku")
        elif choice == "2":
            crud_menu(USER_FILE, "user")
        elif choice == "3":
            peminjaman_menu(ll_peminjaman)
        elif choice == "0":
            print("\nLogging out...")
            pause()
            break
    