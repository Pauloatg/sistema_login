# CONEXÃO COM O BANCO

import psycopg2
import os

os.environ["PGCLIENTENCODING"] = "utf-8"

def conectar():
    conn = psycopg2.connect(
        host="db.amazefwspoodwukdaycx.supabase.co",
        database="postgres",
        user="postgres",
        password="Seculovinte1",  # 🔥 coloca a senha real
        port="5432",
        sslmode="require"  # ⚠️ obrigatório no Supabase
    )
    return conn

from database import conectar

conn = conectar()

print("Conexão concedida!")