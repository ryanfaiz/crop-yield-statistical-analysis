import os
import pandas as pd
import kagglehub
from dotenv import load_dotenv
import subprocess
from pathlib import Path

load_dotenv()

dataset_path = os.getenv("DATASET_PATH")

def setup_dataset():
    """Pastikan dataset tersedia dan path tersimpan di .env"""
    load_dotenv()
    dataset_path = os.getenv("DATASET_PATH")

    if dataset_path is None:
        print("Dataset belum ditemukan. Mengunduh dari Kaggle...")
        path = kagglehub.dataset_download("samuelotiattakorah/agriculture-crop-yield")

        for file in os.listdir(path):
            if file.endswith(".csv"):
                dataset_path = os.path.join(path, file)
                break

        with open(".env", "a") as f:
            f.write(f"\nDATASET_PATH={dataset_path}")

    print("Dataset digunakan dari:", dataset_path)
    return dataset_path

# 2. Menu pilihan pengujian
def main():
    setup_dataset()

    menu = {
        "1": "uji_t.py",
        "2": "uji_anova.py",
        "3": "uji_regresi.py",
        "4": "uji_chi_square.py",
    }

    scripts_dir = Path(__file__).resolve().parent / "scripts"

    while True:
        print("\n=== Menu Pengujian ===")
        print("1. Uji T")
        print("2. ANOVA")
        print("3. Korelasi & Regresi")
        print("4. Chi-Square")
        print("0. Keluar")

        choice = input("Pilih pengujian (0-4): ").strip()

        if choice == "0":
            print("Program selesai. Terima kasih!")
            break

        if choice in menu:
            script_path = scripts_dir / menu[choice]
            print(f"\nMenjalankan {script_path.name}...\n")
            subprocess.run(["python", str(script_path)])
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
