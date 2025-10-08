import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind, levene, f, t
import os
from pathlib import Path
from dotenv import load_dotenv

# === Fungsi bantu untuk format p-value ===
def format_p(p):
    return f"{p:.4e}" if p > 1e-308 else "< 1e-308 (sangat signifikan)"

# 1. Load dataset
load_dotenv()
dataset_path = os.getenv("DATASET_PATH")
if dataset_path is None:
    raise ValueError("DATASET_PATH tidak ditemukan di .env. Jalankan main.py dulu untuk setup dataset.")

df = pd.read_csv(dataset_path)

# 2. Pisahkan data berdasarkan penggunaan pupuk
fert_yes = df[df["Fertilizer_Used"] == True]["Yield_tons_per_hectare"].dropna()
fert_no  = df[df["Fertilizer_Used"] == False]["Yield_tons_per_hectare"].dropna()

# === 3. Perhitungan Statistik Dasar per Kelompok ===
stats = pd.DataFrame({
    "Kelompok": ["Tanpa Pupuk", "Dengan Pupuk"],
    "Mean": [fert_no.mean(), fert_yes.mean()],
    "Median": [fert_no.median(), fert_yes.median()],
    "Std Deviasi": [fert_no.std(), fert_yes.std()],
    "Variance": [fert_no.var(), fert_yes.var()],
    "Jumlah Data (n)": [len(fert_no), len(fert_yes)]
})

# === 4. Uji F (Homogenitas Varians) ===
f_stat, f_pvalue = levene(fert_yes, fert_no, center='mean')
alpha = 0.05
df1 = len(fert_yes) - 1
df2 = len(fert_no) - 1
f_tabel = f.ppf(1 - alpha, df1, df2)
equal_var = f_pvalue > alpha

# === 5. Uji T (Perbedaan Rata-rata) ===
t_stat, t_pvalue = ttest_ind(fert_yes, fert_no, equal_var=equal_var)
t_tabel = t.ppf(1 - alpha/2, df1 + df2)

# === 6. Cetak Hasil Lengkap ===
print("\n=== STATISTIK DESKRIPTIF PER KELOMPOK ===")
print(stats.to_string(index=False))

print("\n=== UJI F (Levene's Test) ===")
print(f"Fhitung: {f_stat:.4f}")
print(f"Ftabel (α=0.05): {f_tabel:.4f}")
print(f"P-value: {format_p(f_pvalue)}")
print("Keputusan:", "Gagal tolak H0 (Varians homogen)" if equal_var else "Tolak H0 (Varians tidak homogen)")

print("\n=== UJI T (Independent Samples T-Test) ===")
print(f"Thitung: {t_stat:.4f}")
print(f"Ttabel (α=0.05, two-tailed): {t_tabel:.4f}")
print(f"P-value: {format_p(t_pvalue)}")
if t_pvalue < alpha:
    print("Keputusan: Tolak H0 → Ada perbedaan signifikan antara lahan dengan pupuk dan tanpa pupuk.")
else:
    print("Keputusan: Gagal tolak H0 → Tidak ada perbedaan signifikan.")

# === 7. Visualisasi: Multiple Vertical Bar Chart (3 kelompok X, 2 batang per kelompok) ===
metrics = ["Mean", "Median", "Std Deviasi"]
x = np.arange(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 6))

# Data per kelompok
tanpa_pupuk = [stats.loc[0, "Mean"], stats.loc[0, "Median"], stats.loc[0, "Std Deviasi"]]
dengan_pupuk = [stats.loc[1, "Mean"], stats.loc[1, "Median"], stats.loc[1, "Std Deviasi"]]

plt.bar(x - bar_width/2, tanpa_pupuk, width=bar_width, label="Tanpa Pupuk", color="#5DADE2")
plt.bar(x + bar_width/2, dengan_pupuk, width=bar_width, label="Dengan Pupuk", color="#58D68D")

# Label dan tampilan
plt.xticks(x, metrics)
plt.ylabel("Nilai (tons per hectare)")
plt.title("Perbandingan Statistik Yield: Tanpa Pupuk vs Dengan Pupuk")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Tambahkan label angka di atas batang
for i in range(len(metrics)):
    plt.text(x[i] - bar_width/2, tanpa_pupuk[i] + 0.05, f"{tanpa_pupuk[i]:.2f}", ha="center", va="bottom")
    plt.text(x[i] + bar_width/2, dengan_pupuk[i] + 0.05, f"{dengan_pupuk[i]:.2f}", ha="center", va="bottom")

# === 8. Autosave grafik ===
script_name = Path(__file__).stem
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"
plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"\nGrafik tersimpan otomatis di: {save_path}")

plt.show()
