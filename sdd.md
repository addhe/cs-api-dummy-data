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
- **Service Layer**
  - Berisi logika bisnis (filter, validasi, transformasi data).
  - Memanggil data access layer.
- **Data Access Layer**
  - Mengelola koneksi dan query ke Supabase.
  - Mengabstraksi detail database dari layer lain.
- **Auth Middleware**
  - Memvalidasi API key/JWT pada setiap request.
- **Error Handler**
  - Menstandarisasi response error.
- **Documentation Module**
  - Swagger/OpenAPI endpoint.

### 5. Data Flow Diagram
1. User mengirim request ke endpoint (dengan autentikasi).
2. Request masuk ke router/controller.
3. Auth middleware memvalidasi autentikasi.
4. Controller memvalidasi input dan meneruskan ke service.
5. Service memproses logika bisnis dan memanggil data access layer.
6. Data access layer melakukan query ke Supabase.
7. Data dikembalikan ke service, lalu ke controller, dan akhirnya ke user.

### 6. Database Design
- Tabel: nasabah (lihat BRD)
- Query menggunakan parameterized query untuk keamanan.

### 7. API Design
- Endpoint: `GET /nasabah`, mendukung query param (id, nama, status).
- Response: JSON, error handling konsisten.

### 8. Security
- Semua endpoint dilindungi autentikasi.
- Validasi input di setiap layer.
- Tidak mengembalikan data sensitif.

### 9. Logging & Monitoring
- Logging request, response, dan error.
- Monitoring uptime (opsional, untuk POC).

### 10. Deployment
- Dapat di-deploy di Vercel/Render/Heroku (opsional, untuk POC).

---
Silakan review SDD ini sebelum implementasi dimulai.
