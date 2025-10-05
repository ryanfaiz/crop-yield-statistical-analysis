import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, linregress
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

# 2. Ambil variabel
x = df["Rainfall_mm"]
y = df["Yield_tons_per_hectare"]

# 3. Korelasi Pearson
corr_coef, p_value_corr = pearsonr(x, y)

print("=== Hasil Uji Korelasi ===")
print("H0: Tidak ada hubungan linear antara Rainfall dan Yield")
print("H1: Ada hubungan linear antara Rainfall dan Yield")
print(f"Koefisien Korelasi Pearson: {corr_coef:.4f}")
print(f"P-value (Korelasi): {format_p(p_value_corr)}")

alpha = 0.05
if p_value_corr < alpha:
    print("Keputusan: Tolak H0 → Ada hubungan signifikan antara Rainfall dan Yield")
else:
    print("Keputusan: Gagal tolak H0 → Tidak ada hubungan signifikan")

# 4. Regresi Linear Sederhana
slope, intercept, r_value, p_value_reg, std_err = linregress(x, y)

print("\n=== Hasil Regresi Linear ===")
print("H0: Koefisien regresi (slope) = 0 → Rainfall tidak memengaruhi Yield")
print("H1: Koefisien regresi (slope) ≠ 0 → Rainfall memengaruhi Yield")
print(f"Persamaan: Yield = {intercept:.4f} + {slope:.4f} * Rainfall_mm")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value (Regresi): {format_p(p_value_reg)}")

if p_value_reg < alpha:
    print("Keputusan: Tolak H0 → Rainfall berpengaruh signifikan terhadap Yield")
else:
    print("Keputusan: Gagal tolak H0 → Rainfall tidak berpengaruh signifikan terhadap Yield")

# 5. Visualisasi: Scatter plot + garis regresi
plt.figure(figsize=(8,6))
sns.scatterplot(x=x, y=y, alpha=0.2, s=10, label="Data")
sns.lineplot(x=x, y=intercept + slope*x, color="red",
             label=f"Y = {intercept:.2f} + {slope:.4f}(X)")
plt.title("Hubungan antara Rainfall dan Yield")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Yield (tons per hectare)")
plt.legend()

# 6. Autosave grafik ke folder output
script_name = Path(__file__).stem
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"

plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"\nGrafik tersimpan otomatis di: {save_path}")

plt.show()
