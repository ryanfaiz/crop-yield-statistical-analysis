# 🌾 Agriculture Crop Yield Analysis

Proyek akhir mata kuliah **Statistika Komputasi – IPB University**.  
Analisis ini menggunakan dataset pertanian untuk memahami faktor-faktor yang memengaruhi hasil panen melalui beberapa uji statistika klasik seperti *T-Test*, *ANOVA*, *Korelasi*, *Regresi*, dan *Chi-Square*.

## 🪪 Penulis
- Ryan Faiz Sanie (J0404241078)

## 📂 Dataset
**Sumber:** [Kaggle – Agriculture Crop Yield](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)

## 📊 Variabel Penelitian
| Variabel | Deskripsi |
|-----------|------------|
| **Region** | Wilayah geografis (North, East, South, West) |
| **Soil_Type** | Jenis tanah (Clay, Sandy, Loam, Silt, Peaty, Chalky) |
| **Crop** | Jenis tanaman (Wheat, Rice, Maize, Barley, Soybean, Cotton) |
| **Rainfall_mm** | Curah hujan (mm) |
| **Temperature_Celsius** | Suhu rata-rata (°C) |
| **Fertilizer_Used** | Penggunaan pupuk (True/False) |
| **Irrigation_Used** | Penggunaan irigasi (True/False) |
| **Weather_Condition** | Kondisi cuaca (Sunny, Rainy, Cloudy) |
| **Days_to_Harvest** | Lama waktu panen (hari) |
| **Yield_tons_per_hectare** | Hasil panen (ton/hektar) |

## 📖 Latar Belakang
Statistika berperan penting dalam mengubah data menjadi informasi bermakna untuk mendukung pengambilan keputusan. Dalam sektor pertanian, hasil panen dipengaruhi oleh banyak faktor seperti jenis tanah, curah hujan, dan suhu. Dengan hadirnya teknologi **IoT** dan **Machine Learning**, data pertanian kini dapat dikumpulkan dan dianalisis secara real-time. Sebagai kampus yang unggul di bidang pertanian dan teknologi, **IPB University** relevan dalam mengintegrasikan statistika, IoT, dan *machine learning* untuk membangun pertanian cerdas (*smart farming*).

## 🎯 Tujuan Analisis
1. Menganalisis perbedaan hasil panen berdasarkan penggunaan pupuk dan jenis tanah.  
2. Mengukur hubungan antara curah hujan dan produktivitas hasil panen.  
3. Mengidentifikasi asosiasi antara jenis tanah dan jenis tanaman.  
4. Mengaplikasikan metode statistika komputasi pada dataset pertanian berskala besar.

## 📈 Hasil Analisis Statistik

### 🔹 1. Uji T (Independent Samples T-Test) + Uji F (Levene’s Test)
**Uji F – Homogenitas Varians:**
- H₀ : Varians kedua kelompok sama (homogen).  
- H₁ : Varians kedua kelompok berbeda (tidak homogen).  

**Hasil Uji F:**
- F-statistic = **0.0815**  
- P-value = **0.7753**  
- **Keputusan Uji F:** Gagal tolak H₀ → Varians homogen → Gunakan uji t dengan equal_var = True.  

**Uji T – Perbandingan Rata-rata:**
- H₀ : Tidak ada perbedaan rata-rata hasil panen antara lahan dengan dan tanpa pupuk.  
- H₁ : Ada perbedaan rata-rata hasil panen antara lahan dengan dan tanpa pupuk.  

**Hasil Uji T:**
- T-statistic = **492.8825**  
- P-value = **< 1e-308 (sangat signifikan)**  
- **Keputusan:** Tolak H₀ → Ada perbedaan rata-rata hasil panen antara lahan dengan pupuk dan tanpa pupuk.  

📊 *Grafik:* [output/uji_t.jpg](output/uji_t.jpg)

---

### 🔹 2. Uji ANOVA (One-Way)
**Hipotesis:**
- H₀ : Rata-rata hasil panen sama pada semua jenis tanah.  
- H₁ : Ada perbedaan rata-rata hasil panen pada minimal satu jenis tanah.  

**Hasil:**
- F-statistic = **0.4604**  
- P-value = **0.8060**  
- **Keputusan:** Gagal tolak H₀ → Tidak ada perbedaan signifikan antar jenis tanah terhadap hasil panen.  

📊 *Grafik:* [output/uji_anova.jpg](output/uji_anova.jpg)

---

### 🔹 3. Uji Korelasi Pearson
**Hipotesis:**
- H₀ : Tidak ada hubungan linear antara curah hujan dan hasil panen.  
- H₁ : Ada hubungan linear antara curah hujan dan hasil panen.  

**Hasil:**
- Koefisien Korelasi (r) = **0.7646**  
- P-value = **< 1e-308 (sangat signifikan)**  
- **Keputusan:** Tolak H₀ → Ada hubungan signifikan antara *Rainfall* dan *Yield*.  

---

### 🔹 4. Regresi Linear Sederhana
**Model:**  
Yield = 1.9039 + 0.0050 × Rainfall_mm  

**Hasil:**
- R² = **0.5846**  
- P-value = **< 1e-308 (sangat signifikan)**  
- **Keputusan:** Tolak H₀ → *Rainfall* berpengaruh signifikan terhadap *Yield*.  

📊 *Grafik:* [output/uji_regresi.jpg](output/uji_regresi.jpg)

---

### 🔹 5. Uji Chi-Square
**Hipotesis:**
- H₀ : Tidak ada asosiasi antara jenis tanah dan jenis tanaman.  
- H₁ : Ada asosiasi antara jenis tanah dan jenis tanaman.  

**Hasil:**
- Chi-Square Statistic = **7.7835**  
- Degrees of Freedom = **5**  
- P-value = **0.1686**  
- **Keputusan:** Gagal tolak H₀ → Tidak ada hubungan signifikan antara jenis tanah dan jenis tanaman.  

📊 *Grafik:* [output/uji_chi_square.jpg](output/uji_chi_square.jpg)

---

## 🧩 Kesimpulan Umum
| Uji | Keputusan | Interpretasi |
|-----|------------|--------------|
| **Uji F + T-Test** | Tolak H₀ (Uji T) | Penggunaan pupuk meningkatkan hasil panen secara signifikan; varians antar kelompok homogen. |
| **ANOVA** | Gagal tolak H₀ | Jenis tanah tidak berpengaruh signifikan terhadap hasil panen. |
| **Korelasi & Regresi** | Tolak H₀ | Curah hujan memiliki hubungan dan pengaruh signifikan terhadap hasil panen. |
| **Chi-Square** | Gagal tolak H₀ | Tidak ada asosiasi signifikan antara jenis tanah dan jenis tanaman. |

---

## 📂 Output Analisis
Semua grafik hasil analisis disimpan otomatis di direktori `output`:
- `uji_t.jpg` — Hasil Uji F + T-Test  
- `uji_anova.jpg` — Hasil ANOVA  
- `uji_regresi.jpg` — Regresi Linear  
- `uji_chi_square.jpg` — Uji Chi-Square  

---

## 💡 Catatan Tambahan
- Semua uji dilakukan menggunakan Python (pandas, scipy, statsmodels, matplotlib).  
- Dataset berukuran besar, sehingga pendekatan *statistika komputasi* digunakan untuk efisiensi perhitungan.  
- Hasil menunjukkan bahwa faktor **pupuk** dan **curah hujan** merupakan variabel paling berpengaruh terhadap produktivitas hasil panen.
