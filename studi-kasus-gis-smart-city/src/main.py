from pathlib import Path
import pandas as pd
import folium

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "laporan_fasilitas_umum.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
REQUIRED = ["id_laporan", "judul", "kategori", "status", "latitude", "longitude", "deskripsi"]
STATUSES = {"Belum ditangani", "Diproses", "Selesai"}

def load_and_validate(path=DATA_PATH):
    data = pd.read_csv(path)
    missing = set(REQUIRED) - set(data.columns)
    if missing:
        raise ValueError(f"Kolom wajib tidak tersedia: {sorted(missing)}")
    data = data.drop_duplicates(subset=["id_laporan"]).copy()
    data["latitude"] = pd.to_numeric(data["latitude"], errors="coerce")
    data["longitude"] = pd.to_numeric(data["longitude"], errors="coerce")
    data = data.dropna(subset=["latitude", "longitude", "kategori", "status"])
    data = data[data["latitude"].between(-90, 90) & data["longitude"].between(-180, 180)]
    data = data[data["status"].isin(STATUSES)]
    return data.reset_index(drop=True)

def create_map(data, path=OUT / "peta_laporan.html"):
    center = [data["latitude"].mean(), data["longitude"].mean()]
    map_view = folium.Map(location=center, zoom_start=13, tiles="OpenStreetMap")
    colors = {"Belum ditangani":"red", "Diproses":"orange", "Selesai":"green"}
    for _, row in data.iterrows():
        popup = (f"<b>{row['judul']}</b><br>ID: {row['id_laporan']}<br>"
                 f"Kategori: {row['kategori']}<br>Status: {row['status']}<br>{row['deskripsi']}")
        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=folium.Popup(popup, max_width=300),
            tooltip=str(row["judul"]),
            icon=folium.Icon(color=colors[row["status"]], icon="info-sign")
        ).add_to(map_view)
    map_view.save(str(path))
    return path

def main():
    data = load_and_validate()
    data.to_csv(OUT / "laporan_bersih.csv", index=False)
    summary = data.groupby(["kategori", "status"]).size().reset_index(name="jumlah_laporan")
    summary.to_csv(OUT / "ringkasan_kategori.csv", index=False)
    map_path = create_map(data)
    print("=== GIS PELAPORAN FASILITAS UMUM ===")
    print(f"Jumlah laporan valid: {len(data)}")
    print("\\nRingkasan kategori dan status:")
    print(summary.to_string(index=False))
    print(f"\\nPeta tersimpan di: {map_path}")
    print("Catatan: data merupakan simulasi.")

if __name__ == "__main__":
    main()
