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
- Pengembangan REST API untuk operasi CRUD (Read, Activate/Deactivate)
- Integrasi dengan database Supabase
- Penambahan kolom `balance` pada tabel nasabah (saldo awal: 117.304.500)
- Endpoint statistik total hadiah dan jumlah peserta aktif
- Endpoint pengiriman email terbatas untuk notifikasi permainan
- Dokumentasi endpoint dan contoh penggunaan

#### Out of Scope:
- Integrasi dengan payment gateway eksternal
- Fitur real-time chat antar peserta
- UI aplikasi frontend untuk peserta

### 4. Functional Requirements
- API dapat mengembalikan seluruh data nasabah
- API dapat mengembalikan data nasabah berdasarkan filter (ID, nama, status)
- API menyediakan endpoint aktivasi/deaktivasi nasabah (`PUT /nasabah/{id}/status`)
- API menyediakan endpoint statistik (`GET /stats`):
  - Total hadiah (jumlah balance seluruh peserta nonaktif)
  - Jumlah peserta aktif
- API menyediakan endpoint pengiriman email terbatas (`POST /email`):
  - Hanya untuk notifikasi sistem
  - Menggunakan template email pra-disetujui
- API memberikan response dalam format JSON
- API memiliki endpoint dokumentasi (Swagger/OpenAPI)

### 5. Non-Functional Requirements
- Response time < 2 detik untuk query sample data
- API hanya dapat diakses oleh user yang terautentikasi
- Rate limiting untuk endpoint pengiriman email (max 5/hari/user)
- Logging request dan error dengan detail transaksi

### 6. Sample Endpoint
- `GET /nasabah` : Mengambil seluruh data nasabah
- `GET /nasabah?id=123` : Mengambil data nasabah berdasarkan ID
- `GET /nasabah?nama=John` : Mengambil data nasabah berdasarkan nama
- `PUT /nasabah/{id}/status` : Mengaktifkan/menonaktifkan nasabah
- `GET /stats` : Mendapatkan statistik permainan
- `POST /email` : Mengirim notifikasi email sistem

### 7. Success Criteria
- API dapat mengembalikan data nasabah sesuai dengan filter yang diberikan (ID, nama, status)
- Response time konsisten di bawah 2 detik untuk dataset sampel
- Dokumentasi API (Swagger) tersedia dan dapat diakses melalui endpoint `/docs`
- Hanya pengguna terautentikasi yang dapat mengakses endpoint API
- Error handling yang konsisten dan informatif untuk semua skenario gagal
- Endpoint aktivasi/deaktivasi berfungsi sesuai ekspektasi
- Statistik hadiah (akumulasi balance peserta kalah) terupdate real-time
- Pengiriman email terbatas berfungsi tanpa abuse

### 8. Supabase Database Schema (POC)
Tabel: nasabah

| Kolom    | Tipe Data   | Keterangan           |
|----------|-------------|----------------------|
| id       | integer     | Primary Key, auto-increment |
| nama     | text        | Nama nasabah         |
| email    | text        | Email nasabah        |
| status   | text        | Status (aktif/nonaktif) |
| balance  | numeric     | Saldo permainan (default: 117304500) |
| created_at | timestamp | Waktu pembuatan data |

Contoh query pembuatan tabel di Supabase:
```sql
create table nasabah (
  id serial primary key,
  nama text not null,
  email text not null,
  status text not null default 'nonaktif',
  balance numeric not null default 117304500,
  created_at timestamp default now()
);
```

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
