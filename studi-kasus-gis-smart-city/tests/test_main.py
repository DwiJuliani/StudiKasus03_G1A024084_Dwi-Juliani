import unittest, sys, tempfile
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from main import load_and_validate

class TestValidation(unittest.TestCase):
    def test_dataset_coordinates_are_valid(self):
        df = load_and_validate()
        self.assertGreater(len(df), 0)
        self.assertTrue(df["latitude"].between(-90, 90).all())
        self.assertTrue(df["longitude"].between(-180, 180).all())

    def test_invalid_coordinate_is_removed(self):
        df = pd.DataFrame([{"id_laporan":"X","judul":"Tes","kategori":"Jalan",
          "status":"Belum ditangani","latitude":200,"longitude":102,"deskripsi":"uji"}])
        with tempfile.NamedTemporaryFile(suffix=".csv", mode="w", encoding="utf-8", delete=False) as f:
            df.to_csv(f.name, index=False)
            p = Path(f.name)
        try:
            self.assertEqual(len(load_and_validate(p)), 0)
        finally:
            p.unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
