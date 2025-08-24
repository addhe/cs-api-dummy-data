# UX/UI Design Flow Documentation
## Project: Simple API for Querying Nasabah Data (Supabase)

### 1. Purpose
Dokumen ini menjelaskan alur penggunaan API dari sudut pandang pengguna (developer/internal team) termasuk contoh request dan response.

### 2. API Interaction Flow
1. Pengguna mengakses dokumentasi API (Swagger UI) di `/docs`.
2. Pengguna memilih endpoint yang ingin diuji (misal: `GET /nasabah`).
3. Pengguna memasukkan parameter query (jika diperlukan) dan API key di header.
4. Pengguna mengklik "Try it out" untuk mengirim request.
5. API mengembalikan response dalam format JSON.

### 3. Example Request & Response
**Request (GET Nasabah):**
```
GET /nasabah?nama=John HTTP/1.1
Authorization: Bearer <token>
```

**Response (GET Success):**
```json
[
  {
    "id": 1,
    "nama": "John Doe",
    "email": "john@example.com",
    "status": "aktif",
    "balance": 117304500
  }
]
```

**Request (PUT Status):**
```
PUT /nasabah/1/status HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "status": "aktif"
}
```

**Response (PUT Success):**
```json
{
  "id": 1,
  "nama": "John Doe",
  "email": "john@example.com",
  "status": "aktif",
  "balance": 117304500
}
```

**Request (GET Stats):**
```
GET /stats HTTP/1.1
Authorization: Bearer <token>
```

**Response (GET Stats):**
```json
{
  "total_hadiah": 586522500,
  "total_peserta_aktif": 5
}
```

**Request (POST Email):**
```
POST /email HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{
  "to": "player@example.com",
  "template_id": "game_notification"
}
```

**Response (POST Email Success):**
```json
{
  "status": "accepted",
  "message": "Email akan diproses"
}
```

**Response (Rate Limit Exceeded):**
```json
{
  "error": "Too Many Requests",
  "message": "Batas pengiriman email harian terlampaui (max 5)"
}
```

### 4. Swagger UI Implementation
- Endpoint dokumentasi tersedia di `/docs`
- Menggunakan OpenAPI 3.0 specification
- Auto-generated dari kode sumber (via FastAPI/Express middleware)
- Mendukung authentication testing dengan API key field
- Menampilkan contoh request/response untuk semua endpoint termasuk email dan statistik

### 5. User Experience Considerations
- Format response JSON konsisten untuk semua endpoint
- Pesan error informatif dengan kode status HTTP yang sesuai
- Dokumentasi parameter query dengan contoh nilai
- Validasi input real-time di Swagger UI
- Rate limiting jelas ditampilkan di dokumentasi endpoint email
- Template ID yang valid terdaftar di dokumentasi
