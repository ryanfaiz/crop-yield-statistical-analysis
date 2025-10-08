import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f_oneway, f
import os
from pathlib import Path
from dotenv import load_dotenv

# === Fungsi bantu untuk format p-value ===
def format_p(p):
    return f"{p:.4e}" if p > 1e-308 else "< 1e-308 (sangat signifikan)"

# === 1. Load dataset ===
load_dotenv()
dataset_path = os.getenv("DATASET_PATH")
if dataset_path is None:
    raise ValueError("DATASET_PATH tidak ditemukan di .env. Jalankan main.py dulu untuk setup dataset.")

df = pd.read_csv(dataset_path)

# === 2. Kelompokkan data berdasarkan Soil_Type ===
soil_types = df["Soil_Type"].unique()
groups = [df[df["Soil_Type"] == soil]["Yield_tons_per_hectare"].dropna() for soil in soil_types]

# === 3. Hitung statistik deskriptif per jenis tanah ===
stats = pd.DataFrame({
    "Soil_Type": soil_types,
    "Mean": [g.mean() for g in groups],
    "Median": [g.median() for g in groups],
    "Std Deviasi": [g.std() for g in groups],
    "Variance": [g.var() for g in groups],
    "Jumlah Data (n)": [len(g) for g in groups]
})

# === 4. Hitung komponen ANOVA secara manual ===
k = len(groups)  # banyak kelompok
N = sum(len(g) for g in groups)  # total sampel
df_between = k - 1
df_within = N - k
grand_mean = df["Yield_tons_per_hectare"].mean()

# Sum of Squares
ss_between = sum(len(g) * (g.mean() - grand_mean) ** 2 for g in groups)
ss_within = sum(sum((g - g.mean()) ** 2) for g in groups)
ss_total = ss_between + ss_within

# Mean Square
ms_between = ss_between / df_between
ms_within = ss_within / df_within

# F hitung dan Ftabel
f_stat = ms_between / ms_within
alpha = 0.05
f_tabel = f.ppf(1 - alpha, df_between, df_within)

# P-value
_, p_value = f_oneway(*groups)

# === 5. Cetak tabel hasil ANOVA ===
anova_table = pd.DataFrame({
    "Sumber Keragaman": ["Between (Antarkelompok)", "Within (Dalam Kelompok)", "Total"],
    "df": [df_between, df_within, df_between + df_within],
    "Sum of Squares": [ss_between, ss_within, ss_total],
    "Mean Square": [ms_between, ms_within, None],
    "F hitung": [f_stat, None, None],
    "F tabel (0.05)": [f_tabel, None, None]
})

print("\n=== TABEL HASIL ANALISIS VARIANSI (ANOVA) ===")
print(anova_table.to_string(index=False, float_format=lambda x: f"{x:,.4f}" if pd.notnull(x) else ""))

# Interpretasi hasil
if p_value < alpha:
    keputusan = "Tolak H0 → Ada perbedaan rata-rata hasil panen antar jenis tanah."
else:
    keputusan = "Gagal tolak H0 → Tidak ada perbedaan signifikan antar jenis tanah."

print("\nP-value:", format_p(p_value))
print("Keputusan:", keputusan)

# === 6. Visualisasi perbandingan statistik (Mean, Median, Std Deviasi) ===
metrics = ["Mean", "Median", "Std Deviasi"]
x = np.arange(len(metrics))
bar_width = 0.12

plt.figure(figsize=(10, 6))

for i, soil in enumerate(soil_types):
    plt.bar(
        x + (i - (len(soil_types) - 1)/2) * bar_width,
        stats.loc[i, metrics],
        width=bar_width,
        label=soil
    )

# Label sumbu dan tampilan
plt.xticks(x, metrics)
plt.ylabel("Nilai Statistik (tons per hectare)")
plt.title("Perbandingan Statistik Yield per Jenis Tanah (Mean, Median, Std Deviasi)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Legend di luar agar tidak terpotong
plt.legend(title="Soil Type", bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

# Label nilai di atas batang
for i, soil in enumerate(soil_types):
    for j, val in enumerate(stats.loc[i, metrics]):
        plt.text(
            x[j] + (i - (len(soil_types) - 1)/2) * bar_width,
            val + 0.05,
            f"{val:.2f}",
            ha="center",
            va="bottom",
            fontsize=7
        )

plt.tight_layout(rect=[0, 0, 0.85, 1])  # beri ruang untuk legend di kanan

# === 7. Autosave grafik ===
script_name = Path(__file__).stem
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"

plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"\nGrafik tersimpan otomatis di: {save_path}")

plt.show()
