import bcrypt
from database import conectar

#------FUNÇÃO DE INSERIR USUARIO------------

def inserir_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()

     # 🔐 Criptografar senha
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
        (nome, email, senha_criptografada)
    )

    conn.commit()
    cursor.close()
    conn.close()

#----------FUNÇÃO DE VERIFICAR LOGIN----------

def verificar_login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome, senha FROM usuarios WHERE email = %s",
        (email,)
    )

    usuario = cursor.fetchone()

    #print("EMAIL DIGITADO:", email)
    #print("USUARIO DO BANCO:", usuario)

    cursor.close()
    conn.close()

    if usuario:
        nome, senha_hash = usuario # 🔥 obrigatório
        senha_hash = bytes(senha_hash)

        try:
            if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
                return nome
        except ValueError:
            print("Hash inválido no banco")    
        
    return None     # Retornar o nome do usuario

#-------BUSCAR USUARIO POR EMAIL-------------

def buscar_usuario_por_email(email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome FROM usuarios WHERE email = %s",
        (email,)
    )

    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario:
        return usuario[0]  # nome
    
    return None