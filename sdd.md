# Software Design Document (SDD)
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Purpose
Dokumen ini menjabarkan struktur teknis secara menyeluruh, termasuk data flow dan modul internal untuk Simple API.

### 2. System Overview
API ini menyediakan akses data nasabah dari database Supabase melalui endpoint REST yang aman dan terdokumentasi.

### 3. System Architecture
- Layered architecture: 
  - Routing/Controller
  - Service/Business Logic
  - Data Access (Supabase)
- Setiap layer terpisah untuk memudahkan maintainability dan scalability.

### 4. Module Breakdown
- **API Router/Controller**
  - Menerima request, validasi input, dan meneruskan ke service.
  - Mengelola response dan error handling.
  - Menambahkan endpoint baru: `/nasabah/{id}/status`, `/stats`, dan `/email`.
- **Service Layer**
  - Berisi logika bisnis (filter, validasi, transformasi data).
  - Memanggil data access layer.
  - Menambahkan modul statistik untuk menghitung total hadiah dan peserta aktif.
  - Menambahkan modul email dengan rate limiting dan validasi template.
- **Data Access Layer**
  - Mengelola koneksi dan query ke Supabase.
  - Mengabstraksi detail database dari layer lain.
  - Menambahkan query khusus untuk menghitung total balance peserta aktif.
- **Auth Middleware**
  - Memvalidasi API key/JWT pada setiap request.
  - Menambahkan role-based access control untuk endpoint kritis.
- **Email Service**
  - Mengintegrasikan dengan layanan email eksternal (misal: SendGrid).
  - Memvalidasi template ID yang disetujui.
  - Menerapkan rate limiting (Redis counter).
  - Mengirim email secara asynchronous.
- **Error Handler**
  - Menstandarisasi response error.
  - Menambahkan kode error khusus untuk rate limiting (429).
- **Documentation Module**
  - Swagger/OpenAPI endpoint.
  - Menambahkan dokumentasi endpoint email dengan contoh template.

### 5. Data Flow Diagram
1. User mengirim request ke endpoint (dengan autentikasi).
2. Request masuk ke router/controller.
3. Auth middleware memvalidasi autentikasi dan hak akses.
4. Controller memvalidasi input dan meneruskan ke service.
5. Service memproses logika bisnis:
   - Untuk `/stats`: menghitung total_hadiah (SUM(balance) dari peserta dengan status 'nonaktif') dan total_peserta_aktif (COUNT peserta dengan status 'aktif')
   - Untuk `/email`: memicu Email Service
6. Data access layer melakukan query ke Supabase.
7. Email Service mengirim ke layanan eksternal (asynchronous).
8. Data dikembalikan ke service, lalu ke controller, dan akhirnya ke user.

### 6. Database Design
- Tabel: nasabah (lihat BRD, termasuk kolom balance)
- Query menggunakan parameterized query untuk keamanan.
- View khusus untuk statistik permainan (opsional untuk optimasi):
  ```sql
  CREATE VIEW game_stats AS
  SELECT 
    SUM(balance) AS total_hadiah,
    (SELECT COUNT(*) FROM nasabah WHERE status = 'aktif') AS total_peserta_aktif
  FROM nasabah
  WHERE status = 'nonaktif';
  ```

### 7. API Design
- Endpoint: 
  - `GET /nasabah` (dengan filter)
  - `PUT /nasabah/{id}/status` (aktivasi/deaktivasi)
  - `GET /stats` (statistik permainan)
  - `POST /email` (pengiriman notifikasi)
- Response: JSON konsisten dengan error codes spesifik.
- Rate limiting diimplementasi menggunakan Redis.

### 8. Security
- Semua endpoint dilindungi autentikasi.
- Validasi input di setiap layer.
- Tidak mengembalikan data sensitif.

### 9. Logging & Monitoring
- Logging request, response, dan error.
- Monitoring uptime (opsional, untuk POC).

### 10. Deployment
- Dapat di-deploy di Vercel/Render/Heroku (opsional, untuk POC).
