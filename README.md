# Peminjaman Studio Cinema Universitas Amikom

🎬 Aplikasi untuk mengelola peminjaman studio di kampus Amikom Yogyakarta.

## Fitur
- Booking studio (1 studio saja tersedia)
- Validasi agar tidak bisa meminjam di waktu yang sama
- Hapus satu peminjaman berdasarkan ID
- Hapus semua data sekaligus
- Simpan otomatis ke `data.json`
- Tampil dengan Streamlit (tanpa Flask)

## Cara Menjalankan
1. Pastikan Python dan Streamlit sudah terinstall:
```bash
pip install streamlit
```

2. Jalankan aplikasi:
```bash
streamlit run main.py
```

## Struktur Folder
- `main.py` → aplikasi utama Streamlit
- `peminjaman.py` → logika dan penyimpanan data
- `data.json` → file penyimpanan
- `README.md` → dokumentasi

# Anggota Kelompok Final Project
<ol>
    <li>M. Firriz Dwinov (24.02.1086)</li>
    <li>M. Iqbal Asidiq (24.02.1080)</li>
    <li>Hafiz Arul Zaky (24.02.1088)</li>
</ol>