from buku import lihat_buku
from sistem import baca_data, clear_screen, pause
from config import BUKU_FILE, USER_FILE
from datetime import datetime

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
        elif choice == "0":
            print("\n✓ Logout berhasil. Sampai jumpa!")
            pause()
            break