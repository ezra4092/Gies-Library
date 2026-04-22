# Gie's Library - Sistem Peminjaman Perpustakaan
Aplikasi CLI berbasis Python untuk manajemen perpustakaan, pengelolaan data buku, dan pelacakan transaksi peminjaman.

## 📋 Overview

Gie's Library adalah sistem informasi perpustakaan yang menyediakan:

- 📚 Manajemen Buku: Pengelolaan koleksi buku perpustakaan secara lengkap.
- 👥 Manajemen Pengguna: Sistem registrasi dan pengelolaan data anggota/pengunjung.
- 🔄 Sistem Peminjaman: Pelacakan transaksi peminjaman dan pengembalian buku secara real-time.

## ✨ Features

- ✅ CLI-based application dengan antarmuka terminal yang rapi
- ✅ Multi-role Login System (Admin & Pengunjung)
- ✅ JSON database (3 file terpisah untuk relasi data yang baik)
- ✅ Complete CRUD operations untuk Admin (Buku, User, Peminjaman)
- ✅ Modular architecture (Pemisahan logika ke dalam folder `app/`)
- ✅ Clear screen & pause utilities untuk user experience yang interaktif

## 📁 Project Structure

```text
Gies-Library/
├── main.py              # Entry point aplikasi
├── config.py            # Konfigurasi & konstanta (Path DB, Kredensial)
├── app/                 # Package modul utama
│   ├── admin.py         # Logika menu dan operasi khusus Admin
│   ├── buku.py          # Pengelolaan entitas dan data buku
│   ├── peminjaman.py    # Logika transaksi pinjam-kembali buku
│   ├── sistem.py        # Utility functions (clear_screen, pause, dll)
│   └── user.py          # Logika pengunjung (login, menu user)
└── data/                # JSON database
    ├── buku_perpus.json # Menyimpan data koleksi buku
    ├── peminjaman.json  # Menyimpan riwayat transaksi
    └── user.json        # Menyimpan akun pengunjung
```

## 🚀 Quick Start

### Prerequisites

Pastikan kamu sudah menginstal Python di komputermu. Tidak ada library eksternal khusus yang dibutuhkan.
```bash
Python 3.6+
```

### Run Application

Jalankan program dari terminal/command prompt:
```bash
python main.py
```

### Admin Login

Gunakan kredensial bawaan berikut untuk masuk ke dashboard Admin (dapat dikonfigurasi di `config.py`):
- Username: `admin`
- Password: `admin123`

## 💻 Usage

### User Flow (Pengunjung)

1. Pilih menu 1. Login pada layar utama.
2. Masukkan kredensial akun pengunjung.
3. Di dalam User Menu, pengunjung dapat:
   - Melihat daftar buku yang tersedia.
   - Melakukan peminjaman buku.
   - Melihat riwayat atau status buku yang sedang dipinjam.

### Admin Flow

1. Pilih menu 2. Login Admin pada layar utama.
2. Masukkan username dan password admin.
3. Di dalam Admin Menu, admin memiliki akses penuh untuk:
   - Kelola Buku: Tambah (Create), Lihat (Read), Edit (Update), Hapus (Delete) buku.
   - Kelola User: Memantau daftar anggota perpustakaan.
   - Kelola Peminjaman: Menyetujui, melacak, atau menyelesaikan status peminjaman buku.

## 📊 Data Structure

Aplikasi menggunakan 3 file JSON utama untuk meniru *Relational Database*.

### 1. Buku (`buku_perpus.json`)
Menyimpan detail katalog buku.
```json
[
  {
    "id_buku": "B001",
    "judul": "Filosofi Teras",
    "penulis": "Henry Manampiring",
    "stok": 5
  }
]
```

### 2. User (`user.json`)
Menyimpan data otentikasi pengunjung.
```json
[
  {
    "id_user": "U001",
    "nama": "Budi Santoso",
    "password": "password123"
  }
]
```

### 3. Peminjaman (`peminjaman.json`)
Melacak relasi antara *User* dan *Buku*.
```json
[
  {
    "id_pinjam": "TRX-001",
    "id_user": "U001",
    "id_buku": "B001",
    "tanggal_pinjam": "2023-10-25",
    "status": "Dipinjam"
  }
]
```

## 🔧 Modules

| Module                 | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| `config.py`            | Path database & kredensial global            |
| `app/sistem.py`        | Utility pendukung interaksi terminal         |
| `app/buku.py`          | Modul pemrosesan objek buku                  |
| `app/peminjaman.py`    | Algoritma kalkulasi dan mutasi stok pinjaman |
| `app/user.py`          | Autentikasi dan navigasi user/pengunjung     |
| `app/admin.py`         | Otentikasi dan pusat kendali CRUD admin      |
| `main.py`              | Entry point & Main Loop aplikasi             |

## ✅ Requirements Checklist

- [x] Berbasis Terminal/CLI
- [x] Database menggunakan format JSON
- [x] Implementasi CRUD (Create, Read, Update, Delete)
- [x] Struktur kode Modular (Package/Modules)
- [x] Role-based Access Control (Admin & Pengunjung)
- [x] Clean & organized file structure

Repository: Gie's Library