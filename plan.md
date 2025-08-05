# Project Plan: CS API Dummy Data

## 1. Tujuan
Membangun API sederhana untuk query data nasabah dari Supabase, lengkap dengan dummy data saldo, siap untuk pengujian, deployment, dan integrasi ke sistem lain.

## 2. Ruang Lingkup
- API endpoint `/nasabah` (GET) dengan filter id, nama, status, email
- Data dummy nasabah (termasuk saldo) otomatis di-populate ke Supabase
- API key authentication
- Unit test dan script test endpoint
- Deployment otomatis ke Google Cloud Run

## 3. Tahapan
1. **Analisis & Dokumentasi**
   - BRD, PRD, TDD, SDD, Deployment Plan, Test Plan
2. **Setup Project**
   - Struktur folder, requirements, .env, .gitignore
3. **Implementasi API**
   - Flask API, Supabase integration, error handling, API key
4. **Populate Dummy Data**
   - Script otomatis insert data nasabah (termasuk saldo)
5. **Unit Testing**
   - Test endpoint, mock supabase, validasi response
6. **Deployment**
   - Dockerfile, deploy script, Cloud Run
7. **Testing & Validasi**
   - Bash/curl test, validasi response, update dokumentasi
8. **Integrasi & Maintenance**
   - Sinkronisasi repo, update README, monitoring

## 4. Deliverables
- API Flask siap deploy
- Script populate dummy data
- Unit test & test script
- Dokumen: BRD, PRD, TDD, SDD, Deployment Plan, Test Plan, README, plan.md
- Pipeline deployment Cloud Run

## 5. Timeline (Estimasi)
| Tahap                | Estimasi |
|----------------------|----------|
| Analisis & Dokumen   | 1 hari   |
| Setup & Implementasi | 1 hari   |
| Populate & Testing   | 1 hari   |
| Deployment & Review  | 1 hari   |

## 6. Risiko & Mitigasi
- **Supabase schema berubah**: update script & API
- **API key bocor**: gunakan .env, jangan commit secret
- **Cloud Run error**: cek log, update Dockerfile
- **Integrasi gagal**: pastikan endpoint & response konsisten

## 7. Catatan
- Semua variabel rahasia di .env
- Kolom saldo harus ada di tabel nasabah Supabase
- Dokumentasi selalu diupdate setiap perubahan signifikan

---

Terakhir update: 5 Agustus 2025