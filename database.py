# CONEXÃO COM O BANCO

import psycopg2
import os
from dotenv import load_dotenv

# 🔥 caminho absoluto do .env
load_dotenv(dotenv_path=r"C:\dev\GitHub\sistema_login\.env")

def conectar():
    print("HOST:", os.getenv("DB_HOST"))  # debug

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )
    return conn
