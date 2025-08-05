import os
from typing import Optional
from flask import Flask, request, jsonify, abort
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
API_KEY = os.environ.get("API_KEY")

supabase: Optional[Client] = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route("/nasabah", methods=["GET"])
def get_nasabah():
    if not supabase:
        abort(500, description="Supabase not configured")
    # API key check
    req_api_key = request.headers.get("x-api-key")
    if not API_KEY or req_api_key != API_KEY:
        abort(401, description="Unauthorized")
    # Query params
    nasabah_id = request.args.get("id", type=int)
    nama = request.args.get("nama", type=str)
    status = request.args.get("status", type=str)
    email = request.args.get("email", type=str)
    query = supabase.table("nasabah").select("id, nama, email, status, saldo, created_at")
    if nasabah_id is not None:
        query = query.filter("id", "eq", nasabah_id)
    if nama is not None:
        query = query.filter("nama", "ilike", f"%{nama}%")
    if status is not None:
        query = query.filter("status", "eq", status)
    if email is not None:
        query = query.filter("email", "eq", email)
    try:
        response = query.execute()
        data = response.data
        return jsonify({"data": data})
    except Exception as e:
        abort(500, description=str(e))

import traceback

@app.errorhandler(Exception)
def handle_exception(e):
    code = 500
    if hasattr(e, 'code'):
        code = e.code
    tb = traceback.format_exc()
    return jsonify({"detail": str(e), "trace": tb}), code

