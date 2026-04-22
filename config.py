import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BUKU_FILE = os.path.join(BASE_DIR, "data", "buku_perpus.json")
USER_FILE = os.path.join(BASE_DIR, "data", "user.json")
PEMINJAMAN_FILE = os.path.join(BASE_DIR, "data", "peminjaman.json")

ADMIN_USN = "admin"
ADMIN_PW = "admin123"
