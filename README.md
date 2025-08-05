# CS API Dummy Data

API sederhana untuk query data nasabah dari Supabase, dilengkapi dummy data saldo, dan siap deploy ke Google Cloud Run.

## Fitur
- Endpoint `/nasabah` untuk query data nasabah (filter: id, nama, status, email)
- Field saldo nasabah tersedia di response
- API key authentication (header: `x-api-key`)
- Dummy data otomatis di-populate ke Supabase
- Unit test siap pakai
- Deployment otomatis ke Cloud Run

## Struktur Project
- `src/main.py` : API utama (Flask)
- `src/init_supabase.py` : Populate dummy data ke Supabase
- `src/test_main.py` : Unit test endpoint
- `deploy_cloudrun.sh` : Script deploy ke Cloud Run
- `test_nasabah_email.sh` : Script test endpoint
- `.env` : Simpan secret (tidak di-commit)

## Setup & Jalankan Lokal
1. Clone repo & masuk ke folder project
2. Buat virtual environment dan install dependensi:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r src/requirements.txt
   ```
3. Copy `.env.example` ke `.env` dan isi variabel Supabase & API key
4. Populate dummy data ke Supabase:
   ```bash
   source venv/bin/activate
   python src/init_supabase.py
   ```
5. Jalankan API lokal:
   ```bash
   source venv/bin/activate
   python src/main.py
   ```

## Deploy ke Cloud Run
```bash
bash deploy_cloudrun.sh
```

## Test Endpoint
```bash
bash test_nasabah_email.sh
```

## Contoh Response
```json
{
  "data": [
    {
      "id": 1,
      "nama": "Addhe Warman Putra",
      "email": "addhe.warman@outlook.co.id",
      "status": "aktif",
      "saldo": 15000000,
      "created_at": "2025-08-05T00:00:00Z"
    }
  ]
}
```

## Catatan
- Pastikan kolom `saldo` sudah ada di tabel `nasabah` Supabase (type: bigint/numeric)
- Semua variabel rahasia diletakkan di `.env` (jangan di-commit)
- Untuk pengembangan, gunakan virtual environment

---

MIT License
