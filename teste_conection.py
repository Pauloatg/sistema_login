from database import conectar

try:
    conn = conectar()
    print("✅ Conectado com sucesso!")
except Exception as e:
    print("❌ Erro:", e)