# FairShare

FairShare é um sistema simples de gerenciamento de despesas compartilhadas, utilizando Django. O foco está na funcionalidade oferecida pelo Django Admin, permitindo criar e gerenciar **carteiras** (Wallets) e **despesas** (Expenses).

## Funcionalidades

- **Usuários Autenticados**: Apenas usuários registrados podem acessar o sistema.
- **Carteiras (Wallets)**:
  - Representam grupos que compartilham despesas.
  - Possuem membros associados.
- **Despesas (Expenses)**:
  - Associadas a uma carteira específica.
  - Incluem informações sobre o pagador e os beneficiários.
- Gerenciamento de dados exclusivamente via **Django Admin**.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Django
- **Banco de Dados**: SQLite (padrão do Django)
- **Interface**: Django Admin (sem front-end personalizado)

## Pré-requisitos

- Python 3.9 ou superior
- Virtualenv ou Conda (recomendado para criar um ambiente virtual)

## Configuração do Projeto

Siga os passos abaixo para configurar e executar o projeto localmente:

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/fairshare.git
cd fairshare
```

### 2. Crie e Ative um Ambiente Virtual

- **Usando venv**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  ```

- **Usando Conda**:
  ```bash
  conda create -n FairShare python=3.9
  conda activate FairShare
  ```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as Migrações do Banco de Dados

```bash
python manage.py migrate
```

### 5. Crie um Superusuário

```bash
python manage.py createsuperuser
```

### 6. Execute o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

Acesse [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) para gerenciar carteiras e despesas.
