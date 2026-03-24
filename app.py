import streamlit as st
import re
from auth import login
from usuarios import verificar_login, buscar_usuario_por_email, inserir_usuario, conectar

#-------Validação de login e senha--------
def email_valido(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def senha_valida(senha):
    return len(senha) >= 6

def nome_valido(nome):
    return len(nome.strip()) >= 10

def usuario_existe(email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM usuarios WHERE email = %s", (email,))
    existe = cursor.fetchone()

    cursor.close()
    conn.close()

    return existe is not None

st.set_page_config(page_title="Sistema", layout="centered")

tab1, tab2 = st.tabs(["Login", "Cadastro"])

# ---------------- LOGIN ---------------- #
with tab1:
    st.subheader("Sistema de Login")

    if "logado" not in st.session_state:
        st.session_state.logado = False

    if "usuario" not in st.session_state:
        st.session_state.usuario = ""

    #-----Msg de logout-------------------
    if "logout_msg" not in st.session_state: 
        #st.success("Logout realizado!")
        st.session_state.logout_msg = False

    if not st.session_state.logado:

        with st.form("form_login"):
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password") #em senha usar tipo, para codoficar

            submitted = st.form_submit_button("Entrar")
            
        if submitted:
            if not email or not senha:
                st.warning("Preencha todos os campos")
            else:   
                nome = verificar_login(email, senha)
                if nome:
                    st.session_state.logado = True
                    st.session_state.usuario = nome # Salva nome
                    st.rerun()
                else:
                    st.error("Email ou senha incorretos", icon="🚫")
    else:
        st.success(f"Bem-vindo, {st.session_state.usuario} 👋")

    #----------------SAIR-----------------------

        if st.button("Sair"):
            st.session_state.logado = False      
            st.session_state.usuario = ""   # Limpa campo
            st.session_state.logout_msg = True  # 👈 cria flag    
            st.rerun()
        st.stop()   #----Resolve o bug-----

#-----------CADASTRAR USUARIO--------------
with tab2:
    st.subheader("Cadastrar Usuário")
    
    #---Mensagem de sucesso (fica no topo)---

    if "cadastro_msg" in st.session_state and st.session_state.cadastro_msg:
        st.success("Usuário cadastrado com sucesso!")
        st.session_state.cadastro_msg = False

    #------inputs SEMPRE visíveis---------
    with st.form("form_cadastro", clear_on_submit=True):
        nome = st.text_input("Nome")
        email = st.text_input("email")
        senha = st.text_input("Senha", type="password")

        submitted = st.form_submit_button("Cadastrar")

    if submitted:
        if not nome or not email or not senha:
                st.warning("Preencha todos os campos")
        elif not nome_valido(nome):
            st.error("Seu Nome deve ter pelo menos 20 caracteres")
        elif not email_valido(email):
            st.error("Email invalido")
        elif not senha_valida(senha):
            st.error("Senha deve ter pelo menos 6 caracteres")
        elif usuario_existe(email):
            st.error("Email já cadastrado")

        else:
            try:
                inserir_usuario(nome, email, senha)
                #----MSG após reload
                st.session_state.cadastro_msg = True
                st.rerun()

            except Exception as e:
                st.error(f"Erro ao cadastrar: {e}")
                    
