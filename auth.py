from database import conectar

#------AUTENTICAÇÃO LOGIN E LOGOUT

def login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
    cursor.execute(query,(email, senha))

    usuario = cursor.fetchone()

    cursor.close()
    conn.close()
    
    if usuario:
        return True
    else:
        return False
