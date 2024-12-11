
# Final Project Kelompok 3 Data Mining

Penelitian ini bertujuan untuk melakukan analisis sentimen dan membangun model klasifikasi serta prediksi yang mampu menentukan kesesuaian antara opini yang diberikan pengguna dengan rating yang mereka berikan. Melalui pendekatan ini, diharapkan dapat diidentifikasi faktor-faktor utama yang mempengaruhi kepuasan pengguna. Selain itu, hasil analisis ini juga akan memberikan rekomendasi strategis untuk meningkatkan kualitas layanan aplikasi MyBCA dan meningkatkan kepuasan pengguna secara keseluruhan.


## Dosen Pengampu
- Amalia Anjani Arifiyanti, S.Kom, M.Kom

## Anggota
- [Andhika Rizky Aulia - 21082010171](https://github.com/ndikrp)
- [Adimas Syiraa Setiabudhi - 21082010172](https://github.com/samidss56)


## Keterangan Isian

#### List Folder Dataset

```
  Dataset
  Stopwords
```

| Name | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `myBca.csv` | `Csv` | Dataset yang sudah di clean dan siap untuk di training |
| `unclean_myBca.csv` | `Csv` | Dataset yang diambil menggunakan metode web scraping, dan belum dilakukan cleaning data |'
| `unclean_myBca.txt` | `Txt` | Informasi mengenai dataset unclean_myBca beserta atribut |
| `stopwords.txt` | `Txt` | Berisi kata yang diabaikan dalam pemrosesan dan biasanya disimpan di dalam stop lists. |

#### List Coding
```
  Data Scraping, Understanding, dan Preparation
  Model Klasifikasi
  Deploy Model
  3 Skenario Model (Optional)
```

| Name | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `EDA.ipynb`      | `ipynb` | Berisi code untuk men scraping data review pengguna dari playstore dan appstore, melakukan proses EDA, dan Data Preparation |
| `Classification_Model.ipynb`      | `ipynb` | Berisi code untuk pemodelan klasifikasi sentimen dari dataset myBca.csv menggunakan algoritma SVM dengan metode pelabelan TextBlob|
| `Model_Deployment.ipynb`      | `ipynb` | Berisi code untuk men deploy model menggunakan streamlit |
| `3_ScenarioModel_(Opt).ipynb`      | `ipynb` | Berisi 4 skenario yang digunakan dalam pemodelan. Menggunakan dataset myBca.csv dengan algoritma Naive Bayes, Logistic Regression, Support Vector Machine (SVM), dan Random Forest menggunakan metode pelabelan TextBlob|



## Progress

- 12/5/2024 - Menentukan Studi Kasus (MyBca)

- 12/6/2024 - Melakukan Pre-Processing

- 12/7/2024 - Melakukan Pemodelan dan Klasifikasi 

- 12/8/2024 - Melakukan Evaluasi Model

- 12/9/2024 - Melakukukan Deployment Model pada Streamlit dan Pembuatan Laporan

- 12/12/2024 - Melakukukan Revisi untuk Menambahkan Skenario

- 12/13/2024 - Melakukan Revisi Evaluasi Model 

- 12/14/2024 - Melakukukan Deployment Ulang Model pada Streamlit dan Pembuatan Laporan

- 12/15/2024 - Penyusunan Laporan

- 12/6/2024 - Penyelesaian Laporan

