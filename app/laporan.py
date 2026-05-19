from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from app.sistem import baca_data, pause
from config import BUKU_FILE, USER_FILE, PEMINJAMAN_FILE


def cetak_laporan_pdf():
    while True:
        print("\n" + "=" * 50)
        print("Cetak Laporan PDF")
        print("=" * 50)
        print("1. Laporan Buku")
        print("2. Laporan Pengunjung")
        print("3. Laporan Peminjaman")
        print("0. Kembali")

        pilihan = input("\nPilih: ").strip()

        if pilihan == "1":
            laporan_buku_pdf()

        elif pilihan == "2":
            laporan_user_pdf()

        elif pilihan == "3":
            laporan_peminjaman_pdf()

        elif pilihan == "0":
            break

        else:
            print("\nPilihan tidak valid!")
            pause()

def laporan_buku_pdf():
    data = baca_data(BUKU_FILE)
    from datetime import datetime

    pdf = SimpleDocTemplate("laporan_buku.pdf")

    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("LAPORAN DATA BUKU", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    tanggal_cetak = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    tanggal = Paragraph(
        f"Tanggal Cetak: {tanggal_cetak}",
        styles['Normal']
    )

    elements.append(tanggal)
    elements.append(Spacer(1, 12))

    table_data = [
        ["ID Buku", "Judul Buku", "Penulis", "Kategori", "Stok"]
    ]

    for buku in data:
        table_data.append([
            buku["id_buku"],
            buku["judul_buku"],
            buku["nama_penulis"],
            buku["kategori"],
            str(buku["stok"])
        ])

    table = Table(table_data, colWidths=[70, 150, 120, 100, 50])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ]))

    elements.append(table)

    pdf.build(elements)

    print("\nPDF laporan buku berhasil dibuat!")
    pause()

def laporan_user_pdf():
    data = baca_data(USER_FILE)
    from datetime import datetime

    pdf = SimpleDocTemplate("laporan_pengunjung.pdf")

    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("LAPORAN DATA PENGUNJUNG", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    tanggal_cetak = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    tanggal = Paragraph(
        f"Tanggal Cetak: {tanggal_cetak}",
        styles['Normal']
    )

    elements.append(tanggal)
    elements.append(Spacer(1, 12))

    table_data = [
        ["ID User", "Nama", "Username", "Member"]
    ]

    for user in data:
        table_data.append([
            user["id_user"],
            user["nama"],
            user["username"],
            user["member"]
        ])

    table = Table(table_data, colWidths=[80, 150, 150, 80])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ]))

    elements.append(table)

    pdf.build(elements)

    print("\nPDF laporan pengunjung berhasil dibuat!")
    pause()

def laporan_peminjaman_pdf():
    data = baca_data(PEMINJAMAN_FILE)
    from datetime import datetime

    pdf = SimpleDocTemplate("laporan_peminjaman.pdf")

    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("LAPORAN DATA PEMINJAMAN", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    tanggal_cetak = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    tanggal = Paragraph(
        f"Tanggal Cetak: {tanggal_cetak}",
        styles['Normal']
    )

    elements.append(tanggal)
    elements.append(Spacer(1, 12))

    table_data = [
        ["Username", "Judul Buku", "Tanggal Pinjam"]
    ]

    for item in data:
        table_data.append([
            item["username"],
            item["judul_buku"],
            item["tanggal_peminjaman"]
        ])

    table = Table(table_data, colWidths=[120, 220, 120])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),

        ('GRID', (0, 0), (-1, -1), 1, colors.black),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ]))

    elements.append(table)

    pdf.build(elements)

    print("\nPDF laporan peminjaman berhasil dibuat!")
    pause()