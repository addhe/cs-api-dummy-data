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
  - Query seluruh data nasabah.
  - Mendukung filter: id, nama, status (via query params).
  - Response: JSON array of nasabah.
- Autentikasi:
  - Header: `Authorization: Bearer <token>` atau `x-api-key: <key>`
- Error Handling:
  - 401 Unauthorized jika tidak ada/mismatch token.
  - 400 Bad Request untuk parameter tidak valid.
  - 500 Internal Server Error untuk error tak terduga.

### 5. Database Schema
- Tabel: nasabah (lihat BRD)

### 6. Sequence Diagram (Simplified)
1. User mengirim request ke endpoint API dengan autentikasi.
2. API memvalidasi autentikasi.
3. API memproses query parameter (jika ada).
4. API melakukan query ke Supabase.
5. API mengembalikan response JSON ke user.

### 7. Security
- Semua endpoint dilindungi autentikasi.
- Validasi input untuk mencegah SQL Injection.
- Tidak mengembalikan data sensitif selain yang didefinisikan.

### 8. Logging & Monitoring
- Logging request dan error (console/log file).
- Monitoring uptime (opsional, untuk POC).

### 9. Documentation
- Endpoint terdokumentasi dengan Swagger/OpenAPI.

### 10. Testing
- Unit test untuk fungsi utama (opsional, untuk POC).
- Manual test untuk endpoint dan autentikasi.

---
Silakan review TDD ini sebelum implementasi dimulai.
