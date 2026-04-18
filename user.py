from buku import lihat_buku
from sistem import baca_data, clear_screen, pause
from config import BUKU_FILE
from datetime import datetime
from config import USER_FILE

def login_pengunjung():
    data_user = baca_data(USER_FILE)

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user_ditemukan = None

    for user in data_user:
        if user["username"] == username:
            user_ditemukan = user
            break
    
    if user_ditemukan is None:
        print("\n✗ Akun tidak ditemukan! Silakan registrasi terlebih dahulu.")
        pause()
        return False
    
    if user_ditemukan["password"] == password:
        print(f"\n✓ Login berhasil! Selamat datang, {user_ditemukan['nama']}")
        pause()
        return True
    
    else:
        print("\n  ✗ Username atau Password salah!")
        pause()
        return False

def lihat_buku():

    data = baca_data(BUKU_FILE)

    if not data:
        print("\nBelum ada data buku.")
        pause()
        return
    
    while True:
        clear_screen()
        print("=" * 70)
        print("Daftar Buku")
        print("=" * 70)

        print("\nUrutan tampilan:")
        print("1. Kode Buku (A-Z)")
        print("2. Data terbaru")
        print("0. Kembali")

        pilihan = input("\nPilih (1/2): ").strip()

        if pilihan == "1":
            data = sorted(data, key=lambda x: x.get("id_buku", ""))
        elif pilihan == "2":
            data = sorted(
                data, 
                key=lambda x: datetime.strptime(x.get("tanggal", "01-01-2000"), "%d-%m-%Y"),
                reverse=True
            )
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")
            pause()
            continue
        
        clear_screen()
        print("=" * 70)
        print("Daftar Buku")
        print("=" * 70)

        print(f"No. {'Kode Buku':<10} | {'Kategori':<20} | {'Judul Buku':<20} | {'Nama Penulis':<20} | {'Stok':<5} | {'Tanggal':<12}")

        for idx, item in enumerate(data, 1):
            print(f"{idx:<2}. {item['id_buku']:<10} | {item['kategori'][:20]:<20} | {item['judul_buku'][:20]:<20} | {item['nama_penulis'][:20]:<20} | {item['stok']:<5} | {item['tanggal']:<12}")
    
        pause()

def user_menu():
    while True:
        clear_screen()
        print("=" * 50)
        print("Menu Pengunjung")
        print("=" * 50)
        print("1. Lihat daftar buku")
        print("2. Lihat status peminjaman")
        print("0. Logout")

        choice = input("\nPilih: ")

        if choice == "1":
            lihat_buku()
            pause()
        elif choice == "2":
            print("Belum ada, bntr y")
            pause()
            lihat_buku()
        elif choice == "0":
            print("\n✓ Logout berhasil. Sampai jumpa!")
            pause()
            break