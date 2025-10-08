# 🌾 Analisis Statistika Komputasi terhadap Faktor-Faktor yang Mempengaruhi Produktivitas Hasil Panen Menggunakan Dataset Pertanian

Proyek akhir mata kuliah **Statistika Komputasi – Sekolah Vokasi IPB University**.  
Analisis ini menggunakan pendekatan **uji parametrik klasik** (*T-Test*, *ANOVA*, *Korelasi*, dan *Regresi Linear*) untuk memahami pengaruh faktor lingkungan dan teknis terhadap produktivitas hasil panen berbasis data pertanian berskala besar.

---

## 🪪 Penulis
- **Ryan Faiz Sanie (J0404241078)**  
- **Maulana Krisna Wahyu A. (J0404241165)**  

**Program Studi:** Teknologi Rekayasa Komputer  
**Institusi:** Sekolah Vokasi, Institut Pertanian Bogor  
**Tahun:** 2025  

---

## 📂 Dataset
**Sumber:** [Kaggle – Agriculture Crop Yield Dataset](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)  
**Penyusun:** Samuel Oti Attakorah  

Dataset berisi **1.000.000 sampel** data pertanian dengan berbagai variabel lingkungan dan teknis seperti curah hujan, jenis tanah, suhu, penggunaan pupuk, irigasi, serta hasil panen (*yield*). Dataset digunakan untuk eksplorasi dan penerapan metode *statistika komputasi* dalam konteks *smart agriculture*.

---

## 📊 Variabel dalam Dataset
| Variabel | Deskripsi |
|-----------|------------|
| **Region** | Wilayah geografis (North, East, South, West) |
| **Soil_Type** | Jenis tanah (Clay, Sandy, Loam, Silt, Peaty, Chalky) |
| **Crop** | Jenis tanaman (Wheat, Rice, Maize, Barley, Soybean, Cotton) |
| **Rainfall_mm** | Curah hujan selama masa tanam (mm) |
| **Temperature_Celsius** | Suhu rata-rata selama masa tanam (°C) |
| **Fertilizer_Used** | Penggunaan pupuk (True/False) |
| **Irrigation_Used** | Penggunaan irigasi (True/False) |
| **Weather_Condition** | Kondisi cuaca (Sunny, Rainy, Cloudy) |
| **Days_to_Harvest** | Lama waktu hingga panen (hari) |
| **Yield_tons_per_hectare** | Hasil panen (ton/hektar) |

---

## 📈 Hasil Analisis Statistik

### 🔹 1. Uji F dan Uji T (Independent Samples T-Test)
**Tujuan:** Mengetahui apakah terdapat perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk.

#### **Hipotesis Uji F (Levene’s Test)**
- H₀ : Varians kedua kelompok sama (homogen)  
- H₁ : Varians kedua kelompok berbeda (tidak homogen)

#### **Hipotesis Uji T**
- H₀ : Tidak ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk  
- H₁ : Ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk

| Statistik | Nilai |
|------------|--------:|
| Rata-rata Tanpa Pupuk | 3.8995 |
| Rata-rata Dengan Pupuk | 5.3996 |
| Fhitung | 0.0815 |
| Ftabel (α=0.05) | 1.0047 |
| Thitung | 492.8825 |
| Ttabel (α=0.05, dua arah) | 1.9600 |

**Keputusan Uji F:** Gagal tolak H₀ → Varians homogen  
**Keputusan Uji T:** Tolak H₀ → Ada perbedaan signifikan antara kelompok

**Kesimpulan:**  
Varians antar kelompok homogen, namun terdapat **perbedaan signifikan** hasil panen.  
Penggunaan pupuk terbukti **meningkatkan produktivitas hasil panen secara signifikan**.

📊 *Grafik:* [`output/uji_t.jpg`](output/uji_t.jpg)

---

### 🔹 2. Uji ANOVA (One-Way)
**Tujuan:** Mengetahui apakah jenis tanah berpengaruh signifikan terhadap hasil panen.

#### **Hipotesis**
- H₀ : Rata-rata hasil panen sama pada semua jenis tanah  
- H₁ : Ada perbedaan rata-rata hasil panen pada minimal satu jenis tanah

| Sumber Keragaman | df | Sum of Squares | Mean Square | Fhitung | Ftabel (0.05) |
|------------------|----:|---------------:|-------------:|---------:|---------------:|
| Antarkelompok (Between) | 5 | 6.6255 | 1.3251 | 0.4604 | 2.2141 |
| Dalam Kelompok (Within) | 999,994 | 2,878,348.5780 | 2.8784 | — | — |
| Total | 999,999 | 2,878,355.2035 | — | — | — |

**P-value:** 0.8060  
**Keputusan:** Gagal tolak H₀ → Tidak ada perbedaan signifikan antar jenis tanah terhadap hasil panen.  

**Kesimpulan:**  
Jenis tanah tidak berpengaruh nyata terhadap produktivitas hasil panen.  
Hasil panen relatif seragam pada berbagai jenis tanah di dataset ini.

📊 *Grafik:* [`output/uji_anova.jpg`](output/uji_anova.jpg)

---

### 🔹 3. Uji Korelasi dan Regresi Linear
**Tujuan:** Mengetahui hubungan dan pengaruh curah hujan (*Rainfall*) terhadap hasil panen (*Yield*).

#### **Hipotesis Korelasi**
- H₀ : Tidak ada hubungan linear antara curah hujan dan hasil panen  
- H₁ : Ada hubungan linear antara curah hujan dan hasil panen

#### **Hipotesis Regresi**
- H₀ : Koefisien regresi (β) = 0 → Curah hujan tidak berpengaruh terhadap hasil panen  
- H₁ : Koefisien regresi (β) ≠ 0 → Curah hujan berpengaruh terhadap hasil panen

| Statistik | Nilai |
|------------|--------:|
| Koefisien Korelasi (r) | 0.7646 |
| Thitung | 1186.3 |
| Ttabel (α=0.05, dua arah) | 1.960 |
| R² (Koef. Determinasi) | 0.5846 |
| Persamaan Regresi | Y = 1.9039 + 0.0050X |

**Keputusan Korelasi:** Tolak H₀ → Ada hubungan linear signifikan  
**Keputusan Regresi:** Tolak H₀ → Curah hujan berpengaruh signifikan terhadap hasil panen  

**Kesimpulan:**  
Terdapat **hubungan positif kuat** antara curah hujan dan hasil panen.  
Setiap kenaikan 1 mm curah hujan meningkatkan hasil panen sekitar **0.005 ton/ha**.  
Curah hujan menjadi salah satu faktor paling berpengaruh terhadap produktivitas pertanian.

📊 *Grafik:* [`output/uji_regresi.jpg`](output/uji_regresi.jpg)

---

## 🧩 Kesimpulan Umum
| Uji | Keputusan | Interpretasi |
|-----|------------|--------------|
| **Uji F + T-Test** | Tolak H₀ (Uji T) | Penggunaan pupuk meningkatkan hasil panen secara signifikan; varians antar kelompok homogen. |
| **ANOVA** | Gagal tolak H₀ | Jenis tanah tidak berpengaruh signifikan terhadap hasil panen. |
| **Korelasi & Regresi** | Tolak H₀ | Curah hujan memiliki hubungan dan pengaruh signifikan terhadap hasil panen. |

---

## 📂 Output Analisis
Semua grafik hasil analisis disimpan otomatis di direktori `output/`:
- `uji_t.jpg` — Hasil Uji F + T-Test  
- `uji_anova.jpg` — Hasil ANOVA  
- `uji_regresi.jpg` — Hasil Regresi Linear  

---

## 💡 Catatan Tambahan
- Analisis dilakukan menggunakan **Python** (pandas, scipy, matplotlib, seaborn).  
- Dataset berskala besar → pendekatan komputasi digunakan untuk efisiensi dan akurasi.  
- Hasil menunjukkan bahwa **pupuk** dan **curah hujan** merupakan faktor paling berpengaruh terhadap produktivitas hasil panen.
