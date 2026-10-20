# Studi Kasus GIS: Pelaporan Fasilitas Umum

Proyek ini merupakan prototipe sederhana yang terinspirasi dari Materi 3 tentang pemanfaatan GIS di industri dan Smart City. Warga dapat melaporkan masalah fasilitas umum beserta koordinatnya agar petugas lebih mudah melihat lokasi dan memprioritaskan tindak lanjut.

**Catatan:** dataset dan koordinat di proyek ini adalah data simulasi untuk pembelajaran, bukan laporan kejadian nyata.

## Fitur
- Membaca dan memvalidasi data laporan CSV.
- Menghapus ID laporan duplikat dan koordinat yang tidak valid.
- Merangkum laporan menurut kategori dan status.
- Membuat peta interaktif dengan marker berwarna sesuai status.
- Mengekspor data bersih dan ringkasan untuk membantu keputusan.

## Struktur
```text
studi-kasus-gis-smart-city/
├── data/laporan_fasilitas_umum.csv
├── src/main.py
├── tests/test_main.py
├── outputs/
├── requirements.txt
├── README.md
└── .gitignore
```

## Cara menjalankan
Gunakan Python 3.10 atau lebih baru. Dari terminal VS Code pada folder proyek:

```bash
pip install -r requirements.txt
python src/main.py
```

Di Windows, jika `python` tidak dikenali, coba `py src/main.py`.

Menjalankan tes:
```bash
python -m unittest discover -s tests
```

## Keluaran
Program menghasilkan `outputs/laporan_bersih.csv`, `outputs/ringkasan_kategori.csv`, dan `outputs/peta_laporan.html`. Buka file HTML di browser. Peta memakai OpenStreetMap, sehingga koneksi internet diperlukan untuk memuat petanya.

## Hubungan dengan materi
GIS digunakan untuk menghubungkan laporan dengan lokasi geografis. Konsep Smart City diterapkan melalui pencatatan masalah fasilitas umum untuk mendukung tindak lanjut petugas. Python digunakan untuk memproses data dan menghasilkan ringkasan. Untuk penerapan nyata, sistem memerlukan basis data, autentikasi, pengelolaan foto, verifikasi laporan, dan koordinasi antarinstansi.
