# Product Requirements Document (PRD)
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Purpose
Dokumen ini bertujuan untuk mendefinisikan fitur dan fungsionalitas produk Simple API dari sudut pandang pengguna (user/tim internal).

### 2. User Stories
- Sebagai user internal, saya ingin mendapatkan daftar seluruh nasabah agar dapat melakukan analisis data.
- Sebagai user internal, saya ingin mencari data nasabah berdasarkan ID, nama, atau status agar dapat menemukan informasi spesifik dengan cepat.
- Sebagai user internal, saya ingin API mudah digunakan dan terdokumentasi dengan baik agar integrasi berjalan lancar.
- Sebagai user internal, saya ingin hanya user yang terautentikasi yang dapat mengakses data agar data tetap aman.

### 3. Features & Functionalities
- Endpoint untuk mengambil seluruh data nasabah.
- Endpoint untuk mengambil data nasabah berdasarkan filter (ID, nama, status).
- Response API dalam format JSON yang mudah diproses.
- Dokumentasi API (Swagger/OpenAPI) yang mudah diakses.
- Autentikasi sederhana (misal: API key atau JWT).
- Validasi input pada parameter query.
- Penanganan error yang jelas dan informatif.

### 4. User Flow
1. User melakukan autentikasi (mengirim API key/token).
2. User mengakses endpoint API sesuai kebutuhan (list/filter nasabah).
3. API mengembalikan data dalam format JSON.
4. Jika terjadi error (misal: parameter salah, tidak terautentikasi), API mengembalikan pesan error yang jelas.

### 5. Acceptance Criteria
- Semua endpoint dapat diakses sesuai dokumentasi.
- Data yang dikembalikan sesuai dengan filter/query yang diberikan.
- Hanya user terautentikasi yang dapat mengakses API.
- Dokumentasi API tersedia dan mudah dipahami.
- Error handling berjalan dengan baik.

### 6. Non-Functional
- Response time < 2 detik untuk query sample data.
- API dapat diakses minimal 99% uptime selama POC.

### 7. Out of Scope
- Fitur update, delete, atau create data nasabah.
- Integrasi dengan sistem eksternal selain Supabase.