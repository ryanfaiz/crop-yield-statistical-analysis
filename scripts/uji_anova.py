import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
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

# 2. Kelompokkan data berdasarkan Soil_Type
groups = [df[df["Soil_Type"] == soil]["Yield_tons_per_hectare"] 
          for soil in df["Soil_Type"].unique()]

# 3. Lakukan One-Way ANOVA
f_stat, p_value = f_oneway(*groups)
print("=== Hasil Uji ANOVA ===")
print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {format_p(p_value)}")

# 4. Interpretasi hasil
alpha = 0.05
if p_value < alpha:
    keputusan = "Tolak H0 → Ada perbedaan rata-rata hasil panen antar jenis tanah."
else:
    keputusan = "Gagal tolak H0 → Tidak ada perbedaan signifikan antar jenis tanah."
print("Keputusan:", keputusan)

# 5. Visualisasi dengan Boxplot
plt.figure(figsize=(8,6))
sns.boxplot(
    x="Soil_Type",
    y="Yield_tons_per_hectare",
    hue="Soil_Type",
    data=df,
    palette="Set2",
    legend=False
)
plt.legend([],[], frameon=False)  # buang legend dummy
plt.title("Perbandingan Yield berdasarkan Jenis Tanah (Soil_Type)")
plt.xlabel("Soil Type")
plt.ylabel("Yield (tons per hectare)")

# 6. Autosave grafik ke folder output
script_name = Path(__file__).stem
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"

plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"Grafik tersimpan otomatis di: {save_path}")

plt.show()
