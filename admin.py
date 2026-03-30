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

def display_items(items, item_type):
    """Generic display function"""
    if not items:
        print(f"\nBelum ada data {item_type}.")
        return False
    
    print(f"No. {'Kode Buku':<10} | {'Kategori':<20} | {'Judul Buku':<20} | {'Nama Penulis':<20} | {'Stok':<5} | {'Tanggal':<12}") 
    for idx, item in enumerate(items, 1):
        if item_type == "buku":
            print(f"{idx:<2}. {item['id_buku']:<10} | {item['kategori']:<20} | {item['judul_buku']:<20} | {item['nama_penulis']:<20} | {item['stok']:<5} | {item['tgl']:<12}")
    return True
    
def crud_view(file, item_type):
    """Generic view function with sorting option"""
    clear_screen()
    print("=" * 50)
    print("Daftar Buku - Gie's Library")
    print("=" * 50)
    
    data = baca_data(file)
    
    if data:
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
    
    display_items(data, item_type)
    pause()

from datetime import datetime

def crud_add(file, item_type):
    """Generic add function"""
    clear_screen()
    print("=" * 50)
    print(f"Tambah Data {item_type.capitalize()} - Gie's Library")
    print("=" * 50)
    
    if item_type == "buku":
        id_buku = input("\nKode Buku: ").strip()
        kategori = input("Kategori: ").strip()
        judul_buku = input("Judul Buku: ").strip()
        nama_penulis = input("Nama Penulis: ").strip()
        stok = input("Stok: ").strip()
        tgl = datetime.now().strftime("%d-%m-%Y")
        
        new_item = {
            "id_buku": id_buku,
            "kategori": kategori,
            "judul_buku": judul_buku,
            "nama_penulis": nama_penulis,
            "stok": stok,
            "tgl": tgl
        }
        
        data = baca_data(file)
        
        # 🔍 CEK DUPLIKAT ID
        for item in data:
            if item['id_buku'] == id_buku:
                print("\nKode Buku sudah ada! Gunakan Kode yang berbeda.")
                pause()
                return
        
        # kalau tidak ada duplikat, baru ditambah
        data.append(new_item)
        simpan_data(file, data)
        print("\n Data berhasil ditambahkan!")
        pause()

def crud_edit(file, item_type):
    """Generic edit function"""
    clear_screen()
    print("=" * 50)
    print(f"Edit Data {item_type.capitalize()} - Gie's Library")
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
        
        simpan_data(file, data)
        print("\nData berhasil diperbarui!")
        pause()

def crud_delete(file, item_type):   
    """Generic delete function"""
    clear_screen()
    print("=" * 50)
    print(f"Hapus Data {item_type.capitalize()} - Gie's Library")
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
        print(f"Admin - Kelola {item_type}")
        print("=" * 50)
        print("1. Tampilkan Daftar")
        print("2. Tambah Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("0. Kembali")
        
        choice = input("\nPilih (0-4): ").strip()
        
        if choice == "1":
            crud_view(file, item_type)
        elif choice == "2":
            crud_add(file, item_type)
        elif choice == "3":
            crud_edit(file, item_type)
        elif choice == "4":
            crud_delete(file, item_type)
        elif choice == "0":
            break

def admin_menu():
    """Admin main menu"""
    while True:
        clear_screen()
        print("=" * 50)
        print("Dashboard - Gie's Library")
        print("=" * 50)
        print("1. Kelola Data Buku")
        print("2. Kelola Data Pengunjung")
        print("0. Logout")
        
        choice = input("\nPilih (0-2): ").strip()
        
        if choice == "1":
            crud_menu(BUKU_FILE, "buku")
        elif choice == "2":
            crud_menu(USER_FILE, "user")
        elif choice == "0":
            print("\nLogging out...")
            pause()
            break
    