from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
studio_list = []

def waktu_bentrok(tanggal, jam_mulai_baru, jam_selesai_baru):
    for data in studio_list:
        if data['tanggal'] == tanggal:
            # Ambil data lama
            jam_mulai_lama = data['jam_mulai']
            jam_selesai_lama = data['jam_selesai']

            # Konversi ke datetime
            fmt = "%H:%M"
            mulai_baru = datetime.strptime(jam_mulai_baru, fmt)
            selesai_baru = datetime.strptime(jam_selesai_baru, fmt)
            mulai_lama = datetime.strptime(jam_mulai_lama, fmt)
            selesai_lama = datetime.strptime(jam_selesai_lama, fmt)

            # Cek apakah waktu tumpang tindih
            if mulai_baru < selesai_lama and selesai_baru > mulai_lama:
                return True
    return False

@app.route('/studio', methods=['GET'])
def get_all():
    return jsonify(studio_list), 200

@app.route('/studio', methods=['POST'])
def add_studio():
    data = request.get_json()
    tanggal = data['tanggal']
    jam_mulai = data['jam_mulai']
    jam_selesai = data['jam_selesai']

    # Validasi jadwal bentrok
    if waktu_bentrok(tanggal, jam_mulai, jam_selesai):
        return jsonify({"message": "Gagal: Jadwal studio sudah dipinjam pada waktu tersebut."}), 409

    studio_list.append(data)
    return jsonify({"message": "Peminjaman berhasil ditambahkan!"}), 201

@app.route('/studio/<int:index>', methods=['PUT'])
def update_studio(index):
    if index < len(studio_list):
        data = request.get_json()
        tanggal = data['tanggal']
        jam_mulai = data['jam_mulai']
        jam_selesai = data['jam_selesai']

        # Hapus data lama sementara agar tidak bentrok dengan dirinya sendiri
        old_data = studio_list.pop(index)

        # Validasi jadwal bentrok
        if waktu_bentrok(tanggal, jam_mulai, jam_selesai):
            studio_list.insert(index, old_data)  # restore
            return jsonify({"message": "Gagal: Jadwal studio sudah dipinjam pada waktu tersebut."}), 409

        studio_list.insert(index, data)
        return jsonify({"message": "Peminjaman berhasil diupdate!"}), 200
    return jsonify({"message": "Data tidak ditemukan"}), 404

@app.route('/studio/<int:index>', methods=['DELETE'])
def delete_studio(index):
    if index < len(studio_list):
        deleted = studio_list.pop(index)
        return jsonify({"message": "Peminjaman berhasil dihapus", "data": deleted}), 200
    return jsonify({"message": "Data tidak ditemukan"}), 404

if __name__ == '_main_':
    app.run(debug=True)
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