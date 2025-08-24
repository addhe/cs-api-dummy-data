# Product Requirements Document (PRD)
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Purpose
Dokumen ini bertujuan untuk mendefinisikan fitur dan fungsionalitas produk Simple API dari sudut pandang pengguna (user/tim internal).

### 2. User Stories
- Sebagai user internal, saya ingin mendapatkan daftar seluruh nasabah agar dapat melakukan analisis data.
- Sebagai user internal, saya ingin mencari data nasabah berdasarkan ID, nama, atau status agar dapat menemukan informasi spesifik dengan cepat.
- Sebagai admin permainan, saya ingin mengaktifkan/menonaktifkan peserta nasabah untuk mengelola partisipasi dalam permainan.
- Sebagai admin permainan, saya ingin melihat total hadiah (jumlah saldo aktif) dan jumlah peserta aktif untuk memantau progres permainan.
- Sebagai admin permainan, saya ingin mengirim notifikasi email terbatas ke peserta menggunakan template yang telah disetujui.
- Sebagai user internal, saya ingin API mudah digunakan dan terdokumentasi dengan baik agar integrasi berjalan lancar.
- Sebagai user internal, saya ingin hanya user yang terautentikasi yang dapat mengakses data agar data tetap aman.

### 3. Features & Functionalities
- Endpoint untuk mengambil seluruh data nasabah (termasuk balance).
- Endpoint untuk mengambil data nasabah berdasarkan filter (ID, nama, status).
- Endpoint aktivasi/deaktivasi nasabah (`PUT /nasabah/{id}/status`).
- Endpoint statistik permainan (`GET /stats`):
  - Total hadiah (jumlah balance seluruh peserta nonaktif)
  - Jumlah peserta aktif
- Endpoint pengiriman email terbatas (`POST /email`):
  - Hanya untuk notifikasi sistem
  - Menggunakan template email pra-disetujui
  - Rate limiting (max 5/hari/user)
- Response API dalam format JSON yang mudah diproses.
- Dokumentasi API (Swagger/OpenAPI) yang mudah diakses.
- Autentikasi sederhana (misal: API key atau JWT).
- Validasi input pada parameter query.
- Penanganan error yang jelas dan informatif.

### 4. User Flow
1. Admin melakukan autentikasi (mengirim API key/token).
2. Admin mengakses endpoint sesuai kebutuhan:
   - Mengelola status peserta (aktivasi/deaktivasi)
   - Memantau statistik permainan
   - Mengirim notifikasi email
3. API mengembalikan data dalam format JSON.
4. Jika terjadi error (misal: parameter salah, tidak terautentikasi, rate limit exceeded), API mengembalikan pesan error yang jelas.

### 5. Acceptance Criteria
- Endpoint aktivasi/deaktivasi mengubah status nasabah dan memperbarui balance secara akurat.
- Endpoint statistik mengembalikan total hadiah (akumulasi balance peserta kalah) dan jumlah peserta aktif yang terupdate real-time.
- Endpoint pengiriman email hanya menerima template yang disetujui dan menerapkan rate limiting.
- Semua endpoint dapat diakses sesuai dokumentasi.
- Data yang dikembalikan sesuai dengan filter/query yang diberikan.
- Hanya user terautentikasi yang dapat mengakses API.
- Dokumentasi API tersedia dan mudah dipahami.
- Error handling berjalan dengan baik untuk semua skenario.

### 6. Non-Functional
- Response time < 2 detik untuk query sample data.
- API dapat diakses minimal 99% uptime selama POC.
- Rate limiting diterapkan pada endpoint pengiriman email (max 5/hari/user).
- Logging transaksi perubahan status dan pengiriman email.

### 7. Out of Scope
- Integrasi dengan payment gateway eksternal.
- Fitur real-time chat antar peserta.
- UI aplikasi frontend untuk peserta.
- Registrasi nasabah melalui endpoint publik (hanya melalui backend internal).
