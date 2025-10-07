import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, levene
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
fert_yes = df[df["Fertilizer_Used"] == True]["Yield_tons_per_hectare"].dropna()
fert_no  = df[df["Fertilizer_Used"] == False]["Yield_tons_per_hectare"].dropna()

# 3. === UJI F (Levene’s Test for Equality of Variances) ===
f_stat, f_pvalue = levene(fert_yes, fert_no, center='mean')
print("=== Uji F (Levene’s Test for Homogeneity of Variances) ===")
print("H0: Varians kedua kelompok sama (homogen)")
print("H1: Varians kedua kelompok berbeda (tidak homogen)\n")
print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {format_p(f_pvalue)}")

# 4. Tentukan apakah varians dianggap sama atau tidak
alpha = 0.05
equal_var = True if f_pvalue > alpha else False
if equal_var:
    print("Keputusan Uji F: Gagal tolak H0 → Varians homogen → Gunakan uji t dengan equal_var=True\n")
else:
    print("Keputusan Uji F: Tolak H0 → Varians tidak homogen → Gunakan uji t dengan equal_var=False\n")

# 5. === UJI T (Independent Samples T-Test) ===
t_stat, t_pvalue = ttest_ind(fert_yes, fert_no, equal_var=equal_var)

print("=== Hasil Uji T (Independent Samples T-Test) ===")
print("H0: Tidak ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk")
print("H1: Ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk\n")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {format_p(t_pvalue)}")

# 6. Interpretasi hasil uji t
if t_pvalue < alpha:
    keputusan = "Tolak H0 → Ada perbedaan rata-rata hasil panen."
else:
    keputusan = "Gagal tolak H0 → Tidak ada perbedaan signifikan."
print("Keputusan:", keputusan)

# 7. Visualisasi dengan Boxplot
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
plt.title("Perbandingan Yield Berdasarkan Penggunaan Pupuk")
plt.ylabel("Yield (tons per hectare)")

# 8. Autosave grafik ke folder output
script_name = Path(__file__).stem 
output_dir = Path(__file__).resolve().parent / "../output"
output_dir.mkdir(exist_ok=True)
save_path = output_dir / f"{script_name}.jpg"

plt.savefig(save_path, dpi=300, bbox_inches="tight")
print(f"Grafik tersimpan otomatis di: {save_path}")

plt.show()
