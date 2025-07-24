import requests

URL = "http://127.0.0.1:5000/studio"

def tampilkan_menu():
    print("\n=== SISTEM PEMINJAMAN STUDIO CINEMA AMIKOM ===")
    print("1. Lihat Semua Peminjaman")
    print("2. Tambah Peminjaman")
    print("3. Ubah Data Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

def tampilkan_semua():
    res = requests.get(URL)
    data = res.json()
    if data:
        for i, d in enumerate(data):
            print(f"{i+1}. Nama: {d['nama']}, Tanggal: {d['tanggal']}, Jam: {d['jam_mulai']} - {d['jam_selesai']}")
    else:
        print("Belum ada data peminjaman.")

def tambah_peminjaman():
    nama = input("Nama Peminjam: ")
    tanggal = input("Tanggal Peminjaman (YYYY-MM-DD): ")
    jam_mulai = input("Jam Mulai (HH:MM): ")
    jam_selesai = input("Jam Selesai (HH:MM): ")
    payload = {
        "nama": nama,
        "tanggal": tanggal,
        "jam_mulai": jam_mulai,
        "jam_selesai": jam_selesai,
        "studio": "Studio Cinema Amikom"
    }
    res = requests.post(URL, json=payload)
    print(res.json()['message'])

def ubah_peminjaman():
    tampilkan_semua()
    index = int(input("Masukkan nomor data yang akan diubah: ")) - 1
    nama = input("Nama Baru: ")
    tanggal = input("Tanggal Baru (YYYY-MM-DD): ")
    jam_mulai = input("Jam Mulai (HH:MM): ")
    jam_selesai = input("Jam Selesai (HH:MM): ")
    payload = {
        "nama": nama,
        "tanggal": tanggal,
        "jam_mulai": jam_mulai,
        "jam_selesai": jam_selesai,
        "studio": "Studio Cinema Amikom"
    }
    res = requests.put(f"{URL}/{index}", json=payload)
    print(res.json()['message'])

def hapus_peminjaman():
    tampilkan_semua()
    index = int(input("Masukkan nomor data yang akan dihapus: ")) - 1
    res = requests.delete(f"{URL}/{index}")
    print(res.json()['message'])

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == '1':
        tampilkan_semua()
    elif pilihan == '2':
        tambah_peminjaman()
    elif pilihan == '3':
        ubah_peminjaman()
    elif pilihan == '4':
        hapus_peminjaman()
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")