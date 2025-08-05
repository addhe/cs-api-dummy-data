# Business Requirements Document (BRD)
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Background & Purpose
Perusahaan membutuhkan API sederhana untuk mengakses data nasabah yang tersimpan di database Supabase. API ini akan digunakan oleh tim internal untuk keperluan analisis, reporting, dan integrasi dengan sistem lain.

### 2. Objectives
- Menyediakan endpoint API untuk mengambil data nasabah dari Supabase.
- Mendukung query/filter sederhana (misal: berdasarkan nama, ID, status).
- Menjamin keamanan dan otorisasi akses data.

### 3. Scope
#### In Scope:
- Pengembangan REST API sederhana (CRUD Read).
- Integrasi dengan database Supabase.
- Dokumentasi endpoint dan contoh penggunaan.
- Sample data nasabah (minimal: ID, nama, email, status).

#### Out of Scope:
- Fitur update, delete, atau create data nasabah.
- Integrasi dengan sistem eksternal selain Supabase.

### 4. Functional Requirements
- API dapat mengembalikan seluruh data nasabah.
- API dapat mengembalikan data nasabah berdasarkan filter (ID, nama, status).
- API memberikan response dalam format JSON.
- API memiliki endpoint dokumentasi (Swagger/OpenAPI).

### 5. Non-Functional Requirements
- Response time < 2 detik untuk query sample data.
- API hanya dapat diakses oleh user yang terautentikasi.
- Logging request dan error.

### 6. Sample Endpoint
- `GET /nasabah` : Mengambil seluruh data nasabah.
- `GET /nasabah?id=123` : Mengambil data nasabah berdasarkan ID.
- `GET /nasabah?nama=John` : Mengambil data nasabah berdasarkan nama.

### 7. Success Criteria
### 8. Supabase Database Schema (POC)
Tabel: nasabah

| Kolom    | Tipe Data   | Keterangan           |
|----------|-------------|----------------------|
| id       | integer     | Primary Key, auto-increment |
| nama     | text        | Nama nasabah         |
| email    | text        | Email nasabah        |
| status   | text        | Status (aktif/nonaktif) |
| created_at | timestamp | Waktu pembuatan data |

Contoh query pembuatan tabel di Supabase:
```sql
create table nasabah (
  id serial primary key,
  nama text not null,
  email text not null,
  status text not null,
  created_at timestamp default now()
);
```
