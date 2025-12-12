# tugas_individu_3_paw

---

# Product Review Analyzer 

Aplikasi untuk menganalisis sentimen dan meringkas ulasan produk menggunakan AI (Hugging Face & Google Gemini).

## Tech Stack
* **Backend:** Python (Pyramid), SQLAlchemy, PostgreSQL, Hugging Face (ROCm/GPU Support), Google Gemini.
* **Frontend:** React + Vite.
* **Database:** PostgreSQL.

## Fitur
* **Sentiment Analysis:** Deteksi positif/negatif/netral (Multilingual: ID/EN).
* **AI Summary:** Ekstraksi poin penting ulasan menggunakan Google Gemini.
* **History:** Penyimpanan riwayat analisis ke database.
* **Responsive UI:** Tampilan optimal untuk Desktop (Split view) dan Mobile.

## Quick Start

### Backend

* Jalankan server database postgresql, buat db.
* Masuk ke dalam folder backend/ dengan "cd backend".
* Jalankan "./init_project.sh" dengan command "source ./init_project.sh" untuk install package dan masuk venv.
* lalu setting .env (db dan api key) sesuai dengan yang anda punya (perhatikan model pada backend/src/views/review_views.py pastikan api key anda support).
* lalu run "python -m src.main"

### Frontend

* Masuk ke dalam folder frontend/ dengan "cd frontend".
* Jalankan "npm run dev"
* buka websitenya pada link localhost

## Screenshoot

### UI Landscape
![Landscape]()
![Potrait]()

## Identity
Nama : Varasina Farmadani

NIM : 123140107

Kelas : Pengembangan Aplikasi Web RB
