import json

DATA_FILE = "data.json"

class PeminjamanStudio:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.data, file, indent=4)

    def cek_konflik(self, tanggal, waktu):
        for entry in self.data:
            if entry["tanggal"] == tanggal and entry["waktu"] == waktu:
                return True
        return False

    def tambah_peminjaman(self, nama, tanggal, waktu, alasan):
        if self.cek_konflik(tanggal, waktu):
            return False, "Studio sudah dibooking pada waktu tersebut."
        id_peminjaman = len(self.data) + 1
        peminjaman_baru = {
            "id": id_peminjaman,
            "nama": nama,
            "tanggal": tanggal,
            "waktu": waktu,
            "alasan": alasan
        }
        self.data.append(peminjaman_baru)
        self.save_data()
        return True, "Peminjaman berhasil ditambahkan."

    def get_all(self):
        return self.data

    def hapus_semua(self):
        self.data = []
        self.save_data()

    def hapus_per_id(self, id_peminjaman):
        self.data = [item for item in self.data if item["id"] != id_peminjaman]
        for i, item in enumerate(self.data):
            item["id"] = i + 1
        self.save_data()
