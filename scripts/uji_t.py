import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import os
from pathlib import Path
from dotenv import load_dotenv

# === Fungsi bantu untuk format p-value ===
def format_p(p):
    return f"{p:.4e}" if p > 1e-308 else "< 1e-308 (sangat signifikan)"

# 1. Load dataset (gunakan .env agar portable)
load_dotenv()
dataset_path = os.getenv("DATASET_PATH")
if dataset_path is None:
    raise ValueError("DATASET_PATH tidak ditemukan di .env. Jalankan main.py dulu untuk setup dataset.")

df = pd.read_csv(dataset_path)

# 2. Pisahkan data berdasarkan penggunaan pupuk
fert_yes = df[df["Fertilizer_Used"] == True]["Yield_tons_per_hectare"]
fert_no  = df[df["Fertilizer_Used"] == False]["Yield_tons_per_hectare"]

# 3. Lakukan Uji T (Independent Samples T-Test)
t_stat, p_value = ttest_ind(fert_yes, fert_no, equal_var=False)  # Welch’s T-test

# 4. Tampilkan Hipotesis
print("=== Hasil Uji T (Independent Samples T-Test) ===")
print("H0: Tidak ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk")
print("H1: Ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk\n")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {format_p(p_value)}")

# 5. Interpretasi hasil
alpha = 0.05
if p_value < alpha:
    keputusan = "Tolak H0 → Ada perbedaan rata-rata hasil panen."
else:
    keputusan = "Gagal tolak H0 → Tidak ada perbedaan signifikan."
print("Keputusan:", keputusan)

# 6. Visualisasi dengan Boxplot (Seaborn)
plt.figure(figsize=(6,5))
sns.boxplot(
    x="Fertilizer_Used", 
    y="Yield_tons_per_hectare", 
    hue="Fertilizer_Used", 
    data=df, 
    palette="Set2", 
    legend=False
)
plt.xticks([0,1], ["Tanpa Pupuk", "Dengan Pupuk"])
plt.title("Perbandingan Yield")
plt.ylabel("Yield (tons per hectare)")

# 7. Autosave grafik ke folder output (cross-platform)
script_name = Path(__file__).stem 
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"

plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"Grafik tersimpan otomatis di: {save_path}")

plt.show()
