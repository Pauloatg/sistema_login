# 🔐 Sistema de Login com Python + PostgreSQL (Supabase)

Sistema completo de autenticação de usuários desenvolvido em Python, com integração a banco de dados PostgreSQL hospedado no Supabase BD online. O projeto implementa boas práticas de segurança, incluindo uso de variáveis de ambiente e criptografia de senhas com bcrypt.

---

## 🚀 Funcionalidades

* ✅ Cadastro de usuários
* ✅ Login com validação de credenciais
* ✅ Criptografia de senha com bcrypt
* ✅ Conexão com banco PostgreSQL (Supabase)
* ✅ Uso de variáveis de ambiente (.env)
* ✅ Estrutura modular do projeto

---

## 🛠️ Tecnologias utilizadas

* Python 3
* PostgreSQL
* Supabase
* psycopg2
* bcrypt
* python-dotenv
* Streamlit (interface)

---

## 📂 Estrutura do projeto

```
sistema_login/
│
├── app.py              # Interface com Streamlit
├── database.py         # Conexão com banco de dados
├── auth.py             # Lógica de autenticação
├── usuarios.py         # Operações com usuários
├── .env                # Variáveis de ambiente (NÃO versionado)
├── requirements.txt
```

---

## ⚙️ Configuração do ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/Pauloatg/sistema_login.git
cd sistema_login
```
---
### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```
---
### 3. Instalar dependências

```bash
pip install -r requirements.txt
```
---
### 4. Criar arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte formato:

```
DB_HOST=seu_host
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_PORT=5432
```
⚠️ Nunca compartilhe esse arquivo publicamente.
---
## ▶️ Como executar

```bash
python -m streamlit run app.py
```

---

## 🔐 Segurança

* Senhas armazenadas com hash usando bcrypt
* Uso de variáveis de ambiente para proteger credenciais
* Arquivo `.env` ignorado no Git (.gitignore)

---

## 📌 Melhorias futuras

* Implementar autenticação com JWT
* Recuperação de senha
* Deploy em ambiente cloud (Render/Railway)
* Validações avançadas de entrada

---

## 👨‍💻 Autor

Paulo Torres
[GitHub](https://github.com/Pauloatg)

---
