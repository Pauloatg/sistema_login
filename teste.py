import psycopg2

try:
    conn = psycopg2.connect(
        host="db.amazefwspoodwukdaycx.supabase.co",
        database="postgres",
        user="postgres",
        password="Seculovinte1",
        port="5432",
        sslmode="require",
        connect_timeout=5
    )
    print("Conectado com sucesso!")
    conn.close()

except Exception as e:
    print("Erro:", e)