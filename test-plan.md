# Test Plan & Test Cases
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Purpose
Dokumen ini menyusun strategi pengujian untuk memastikan kualitas dan stabilitas API sesuai kebutuhan bisnis dan teknis.

### 2. Test Strategy
- Pengujian dilakukan secara manual dan otomatis (jika memungkinkan).
- Fokus pada pengujian fungsionalitas endpoint, autentikasi, validasi input, dan error handling.
- Pengujian dilakukan pada lingkungan POC/development.

### 3. Test Scope
- In Scope: Semua endpoint API, autentikasi, validasi, response format, error handling.
- Out of Scope: Pengujian integrasi dengan sistem eksternal selain Supabase.

### 4. Test Types
- Functional Testing
- Security Testing (autentikasi, akses data)
- Negative Testing (input salah, tanpa autentikasi)
- Performance Testing (response time sample data)

### 5. Test Cases
| No | Test Case                                      | Langkah Uji                                                                 | Data Uji                | Expected Result                        |
|----|------------------------------------------------|----------------------------------------------------------------------------|-------------------------|----------------------------------------|
| 1  | Get all nasabah (autentikasi valid)            | Kirim GET /nasabah dengan API key/JWT valid                                 | -                       | 200 OK, data nasabah dikembalikan      |
| 2  | Get nasabah by ID (autentikasi valid)          | Kirim GET /nasabah?id=1 dengan API key/JWT valid                            | id=1                    | 200 OK, data nasabah sesuai ID         |
| 3  | Get nasabah by nama (autentikasi valid)        | Kirim GET /nasabah?nama=John dengan API key/JWT valid                       | nama=John               | 200 OK, data nasabah sesuai nama       |
| 4  | Get nasabah by status (autentikasi valid)      | Kirim GET /nasabah?status=aktif dengan API key/JWT valid                    | status=aktif            | 200 OK, data nasabah sesuai status     |
| 5  | Request tanpa autentikasi                      | Kirim GET /nasabah tanpa API key/JWT                                        | -                       | 401 Unauthorized                      |
| 6  | Request dengan API key/JWT tidak valid         | Kirim GET /nasabah dengan API key/JWT salah                                 | -                       | 401 Unauthorized                      |
| 7  | Request dengan parameter tidak valid           | Kirim GET /nasabah?id=abc dengan API key/JWT valid                          | id=abc                  | 400 Bad Request                       |
| 8  | Endpoint tidak ditemukan                      | Kirim GET /nasabahs dengan API key/JWT valid                                | -                       | 404 Not Found                         |
| 9  | Performance test                              | Kirim GET /nasabah dengan data sample >1000 rows                            | -                       | Response < 2 detik                    |

### 6. Test Data
- Data sample nasabah di Supabase (minimal 5 record, variasi id, nama, status).

### 7. Test Environment
- API berjalan di lingkungan development/POC.
- Database Supabase dengan data sample.

### 8. Acceptance Criteria
- Semua test case utama lulus.
- Tidak ada bug kritikal pada fungsionalitas utama.

---
Silakan review test plan & test cases ini sebelum pengujian dilakukan.
