# FastAPI-CRUD-Using-ORM
A FastAPI project for managing notes with user authentication, built with PostgreSQL and Async SQLAlchemy.

## Features

- User registration and login with password hashing
- JWT-based authentication
- CRUD operations for notes
- Async database operations with PostgreSQL
- Configurable via `.env` file

## Requirements

- Python 3.10+
- PostgreSQL
- pip or Poetry

## Setup Instructions

### 1. Clone the repository

<pre>
git clone <https://github.com/mrnyanlinnhtet/FastAPI-CRUD-Using-ORM>
cd FastAPI-CRUD-Using-ORM
</pre>




### 2. Create and activate virtual environment
<pre>python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate </pre>


### 3. Install dependencies
<pre>pip install -r requirements.txt</pre>


### 4. Configure environment variables
<pre>
DATABASE_URL=postgresql+asyncpg://myuser:mypassword@localhost:5432/note
SECRET_KEY=12345
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=6
</pre>


### 5. Create PostgreSQL database
<pre>
psql -U postgres

CREATE DATABASE note;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE note TO myuser;
\q
</pre>


### 6. Create database tables
<pre>python -m app.scripts.create_tables</pre>


### 7. Run the FastAPI server
<pre>uvicorn app.main:app --reload</pre>


## How to Run

- Make sure PostgreSQL is running.
- Activate your virtual environment.
- Make sure .env is configured correctly.
- Run database table creation script (if not already done):
    <pre>python -m app.scripts.create_tables</pre>
- Start the FastAPI server:
    <pre>uvicorn app.main:app --reload</pre>
- Open the browser and access the API docs at:
    <pre>http://127.0.0.1:8000/docs</pre>
- Use endpoints to register users, login, and manage notes.


## Project Structure

<pre>
app/
├── controller/
|  ├── user_controller.py
│  └── note_controller.py
├── model/
|  ├── user_model.py
│  └── note_model.py
├── schemas/
│   ├── user_schema.py
│   └── note_schema.py
|── scripts/
|   ├── create_tables.py
├── service/
|   ├── user_service.py
│   └── note_service.py
├── utils/
|  ├── authentication.py
│  └── password.py
└── main.py
└── database.py
└── config.py
</pre>


## Usage

- Register a user
- Login to receive JWT token
- Create, read, update, and delete notes