import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("SUPABASE_URL and SUPABASE_KEY must be set in environment variables.")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Test connection
try:
    response = supabase.table("nasabah").select("*").limit(1).execute()
    print("Koneksi ke Supabase berhasil.")
except Exception as e:
    print(f"Gagal koneksi ke Supabase atau tabel belum ada: {e}")

# Populate dummy data if table exists
dummy_data = [
    {"nama": "Addhe Warman Putra", "email": "addhe.warman@outlook.co.id", "status": "aktif", "saldo": 15000000000},
    {"nama": "Jane Smith", "email": "jane.smith@example.com", "status": "nonaktif", "saldo": 2500000},
    {"nama": "Budi Santoso", "email": "budi.santoso@example.com", "status": "aktif", "saldo": 5000000},
    {"nama": "Siti Aminah", "email": "siti.aminah@example.com", "status": "aktif", "saldo": 12000000},
    {"nama": "Agus Salim", "email": "agus.salim@example.com", "status": "nonaktif", "saldo": 1000000},
    {"nama": "Eudora Dyrroth", "email": "dyrrotheudora@example.com", "status": "aktif", "saldo": 15000000000},
    {"nama": "Robertus Negoro", "email": "robertusnegoro@example.com", "status": "aktif", "saldo": 10000000000},
    {"nama": "Gandi Tio", "email": "notgandi@example.com", "status": "aktif", "saldo": 10000000000}
]

try:
    for row in dummy_data:
        # Cek apakah data sudah ada berdasarkan email
        exists = supabase.table("nasabah").select("id").eq("email", row["email"]).execute()
        if not exists.data:
            supabase.table("nasabah").insert(row).execute()
        else:
            # Update saldo jika data sudah ada
            supabase.table("nasabah").update({"saldo": row["saldo"], "nama": row["nama"], "status": row["status"]}).eq("email", row["email"]).execute()
    print("Dummy data berhasil di-populate ke tabel nasabah.")
except Exception as e:
    print(f"Gagal populate dummy data: {e}")
