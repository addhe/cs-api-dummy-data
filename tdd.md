# Technical Design Document (TDD)
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Purpose
Dokumen ini menjabarkan pendekatan teknis untuk membangun fitur API sesuai PRD, termasuk arsitektur, teknologi, dan detail implementasi.

### 2. High-Level Architecture
- API berbasis REST, dibangun menggunakan Node.js (Express) atau Python (FastAPI).
- Database Supabase (PostgreSQL) sebagai sumber data utama.
- API terhubung ke Supabase menggunakan library resmi (misal: supabase-js atau supabase-py).
- Autentikasi API menggunakan API key atau JWT.

### 3. Technology Stack
- Backend: Node.js (Express) / Python (FastAPI)
- Database: Supabase (PostgreSQL)
- Dokumentasi: Swagger/OpenAPI
- Deployment: Vercel/Render/Heroku (opsional, untuk POC)

### 4. API Endpoint Design
- `GET /nasabah` :
  - Query seluruh data nasabah (termasuk balance).
  - Mendukung filter: id, nama, status (via query params).
  - Response: JSON array of nasabah.
- `PUT /nasabah/{id}/status` :
  - Mengaktifkan/menonaktifkan status nasabah.
  - Request body: { "status": "aktif" | "nonaktif" }
  - Response: 200 OK dengan data nasabah terupdate.
- `GET /stats` :
  - Mengembalikan statistik permainan.
  - total_hadiah = jumlah balance seluruh peserta nonaktif (kalah)
  - total_peserta_aktif = jumlah peserta dengan status 'aktif'
  - Response: { "total_hadiah": number, "total_peserta_aktif": number }
- `POST /email` :
  - Mengirim notifikasi email sistem.
  - Request body: { "to": "email", "template_id": "id_template" }
  - Rate limiting: max 5/hari/user.
  - Response: 202 Accepted (asynchronous processing).
- Autentikasi:
  - Header: `Authorization: Bearer <token>` atau `x-api-key: <key>`
- Error Handling:
  - 401 Unauthorized jika tidak ada/mismatch token.
  - 400 Bad Request untuk parameter tidak valid.
  - 429 Too Many Requests untuk melebihi rate limit email.
  - 500 Internal Server Error untuk error tak terduga.

### 5. Database Schema
- Tabel: nasabah (lihat BRD, termasuk kolom balance)

### 6. Sequence Diagram (Simplified)
1. User mengirim request ke endpoint API dengan autentikasi.
2. API memvalidasi autentikasi.
3. API memproses query parameter (jika ada).
4. API melakukan query ke Supabase:
   - Untuk `/stats`: menghitung SUM(balance) WHERE status='nonaktif'
5. Untuk endpoint email: API memicu layanan email eksternal.
6. API mengembalikan response JSON ke user.

### 7. Security
- Semua endpoint dilindungi autentikasi.
- Validasi input untuk mencegah SQL Injection.
- Rate limiting pada endpoint pengiriman email.
- Tidak mengembalikan data sensitif selain yang didefinisikan.

### 8. Logging & Monitoring
- Logging request, response, dan error dengan detail transaksi.
- Monitoring penggunaan endpoint email dan statistik permainan.
- Monitoring uptime (opsional, untuk POC).

### 9. Documentation
- Endpoint terdokumentasi dengan Swagger/OpenAPI.
- Contoh penggunaan endpoint email dengan template yang disetujui.

### 10. Testing
- Unit test untuk fungsi utama (opsional, untuk POC).
- Manual test untuk endpoint aktivasi/deaktivasi dan statistik.
- Pengujian rate limiting pada endpoint email.
