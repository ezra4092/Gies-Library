from sistem import baca_data, pause
from config import USER_FILE
from sistem import clear_screen, pause

def login_pengunjung():
    data_user = baca_data(USER_FILE)

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in data_user:
        if user["username"] == username and user["password"] == password:
            print(f"\nLogin berhasil! Selamat datang, {user['nama']}")
            pause()
            return True
        
    print("\nUsername atau password salah!")
    pause()
    return False 

def user_menu():
    while True:
        clear_screen()
        print("=" * 50)
        print("Menu Pengunjung")
        print("=" * 50)
        print("1. Lihat daftar buku")
        print("0. Logout")

        choice = input("\nPilih: ")

        if choice == "1":
            print("Menampilkan daftar buku...")
            pause()
        elif choice == "0":
            print("\nLogout berhasil. Sampai jumpa!")
            pause()
            break