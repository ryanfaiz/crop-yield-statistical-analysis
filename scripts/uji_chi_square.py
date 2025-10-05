import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import os
from pathlib import Path
from dotenv import load_dotenv

# === Fungsi bantu untuk format p-value ===
def format_p(p):
    return f"{p:.4e}" if p > 1e-308 else "< 1e-308 (sangat signifikan)"

# 1. Load dataset (path dari .env agar portable)
load_dotenv()
dataset_path = os.getenv("DATASET_PATH")
if dataset_path is None:
    raise ValueError("DATASET_PATH tidak ditemukan di .env. Jalankan main.py dulu untuk setup dataset.")

df = pd.read_csv(dataset_path)

# 2. Buat tabel kontingensi Soil_Type vs Fertilizer_Used
contingency_table = pd.crosstab(df["Soil_Type"], df["Fertilizer_Used"])

print("=== Tabel Kontingensi ===")
print(contingency_table)

# 3. Lakukan uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print("\n=== Hasil Uji Chi-Square ===")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"Degrees of Freedom: {dof}")
print(f"P-value: {p_value:.4e}")

# 4. Interpretasi hasil
alpha = 0.05
if p_value < alpha:
    keputusan = "Tolak H0 → Ada hubungan signifikan antara Soil_Type dan Fertilizer_Used."
else:
    keputusan = "Gagal tolak H0 → Tidak ada hubungan signifikan."
print("Keputusan:", keputusan)

# 5. Visualisasi dengan Heatmap (observed counts)
plt.figure(figsize=(7,5))
sns.heatmap(contingency_table, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Tabel Kontingensi Soil_Type vs Fertilizer_Used")
plt.xlabel("Fertilizer Used")
plt.ylabel("Soil Type")

# 6. Autosave grafik ke folder output
script_name = Path(__file__).stem
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"

plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"\nGrafik tersimpan otomatis di: {save_path}")

plt.show()
