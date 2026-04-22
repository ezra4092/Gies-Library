

from app.sistem import clear_screen, pause
from app.admin import admin_login, admin_menu
from app.user import login_pengunjung, user_menu

def main_menu():
    """Main menu aplikasi"""
    while True:
        clear_screen()
        print("=" * 50)
        print("Selamat Datang di Gie's Library!")
        print("=" * 50)
        print("1. Login")
        print("2. Login Admin")
        print("0. Exit")
        
        choice = input("\nPilih menu (0-2): ").strip()
        
        if choice == "1":
            if login_pengunjung():
                user_menu()
        elif choice == "2":
            if admin_login():
                admin_menu()
        elif choice == "0":
            clear_screen()
            print("=" * 50)
            print("Terima kasih. Sampai jumpa kembali!")
            print("=" * 50)
            break
        else:
            print("\n✗ Pilihan tidak valid!")
            pause()

if __name__ == "__main__":
    main_menu()
