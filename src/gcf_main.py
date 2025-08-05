# main.py entrypoint for Google Cloud Function
import os
from typing import Optional
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from supabase import create_client, Client
from mangum import Mangum

app = FastAPI(title="Simple API for Querying Nasabah Data (Supabase)")

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
API_KEY = os.environ.get("API_KEY")

supabase: Optional[Client] = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    if not API_KEY or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key

@app.get("/nasabah")
def get_nasabah(
    id: Optional[int] = None,
    nama: Optional[str] = None,
    status: Optional[str] = None,
    api_key: str = Depends(get_api_key)
):
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    query = supabase.table("nasabah")
    if id is not None:
        query = query.eq("id", id)
    if nama is not None:
        query = query.ilike("nama", f"%{nama}%")
    if status is not None:
        query = query.eq("status", status)
    try:
        response = query.select("id, nama, email, status, created_at").execute()
        data = response.data
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(Exception)
def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)}
    )

# Google Cloud Function entrypoint
handler = Mangum(app)

def main(request):
    """Entrypoint for Google Cloud Function HTTP trigger."""
    return handler(request.scope, request.receive, request.send)
