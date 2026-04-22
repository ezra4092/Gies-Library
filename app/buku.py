from app.sistem import baca_data, pause
from config import BUKU_FILE

def lihat_buku():
    data_buku = baca_data(BUKU_FILE)

    if not data_buku:
        print("\nTidak ada data buku.")
        pause()
        return

    print(f"{'📚 DAFTAR BUKU GIE\'S LIBRARY 📚':^{106}}")
    print("=" * 106)
    print(f"| {'No':<5} | {'Judul':<30} | {'Penulis':<25} | {'Stok':^10} | {'Kategori':^20} |")
    print("=" * 106)

    for i, buku in enumerate(data_buku, start=1):
        judul_buku = buku.get("judul_buku", "-")
        nama_penulis = buku.get("nama_penulis", "-")
        stok = buku.get("stok", "-")
        kategori = buku.get("kategori", "-")

        print(f"| {i:<5} | {judul_buku:<30} | {nama_penulis:<25} | {stok:^10} | {kategori:^20} | ")

    print("=" * 106)