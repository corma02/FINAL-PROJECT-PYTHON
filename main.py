import streamlit as st
from peminjaman import PeminjamanStudio

st.set_page_config(page_title="Peminjaman Studio Amikom", page_icon="🎬")
st.title("📽️ Peminjaman Studio Cinema Universitas Amikom")

studio = PeminjamanStudio()

st.header("Formulir Peminjaman")
nama = st.text_input("Nama Peminjam")
tanggal = st.date_input("Tanggal Peminjaman")
waktu = st.selectbox("Waktu", ["08:00-10:00", "10:00-12:00", "13:00-15:00", "15:00-17:00"])
alasan = st.text_area("Alasan Peminjaman")

if st.button("Ajukan Peminjaman"):
    if nama and alasan:
        sukses, pesan = studio.tambah_peminjaman(nama, str(tanggal), waktu, alasan)
        if sukses:
            st.success(pesan)
        else:
            st.error(pesan)
    else:
        st.warning("Mohon lengkapi semua field.")

st.markdown("---")
if st.button("🗑️ Hapus Semua Data"):
    studio.hapus_semua()
    st.success("Semua data berhasil dihapus.")
    st.rerun()

st.header("📋 Daftar Peminjaman")
data = studio.get_all()

if data:
    for entry in data:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"**ID #{entry['id']}** | {entry['tanggal']} {entry['waktu']} - {entry['nama']} - {entry['alasan']}")
        with col2:
            if st.button("Hapus", key=f"hapus_{entry['id']}"):
                studio.hapus_per_id(entry["id"])
                st.success(f"Data dengan ID {entry['id']} berhasil dihapus.")
                st.rerun()
else:
    st.info("Belum ada peminjaman.")
