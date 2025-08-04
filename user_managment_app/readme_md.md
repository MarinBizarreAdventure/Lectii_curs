# User Management API - Clean Architecture

O aplicație FastAPI construită cu Clean Architecture, autentificare JWT și mock database.

## Caracteristici

- ✅ Clean Architecture (Domain, Infrastructure, Presentation)
- ✅ Autentificare JWT
- ✅ CRUD complet pentru useri
- ✅ Mock database (în memorie)
- ✅ Validare cu Pydantic
- ✅ Dependency Injection
- ✅ Teste unitare de bază

## Instalare și Rulare

### 1. Instalare dependințe
```bash
pip install -r requirements.txt
```

### 2. Rulare aplicație
```bash
python main.py
```

Sau cu uvicorn:
```bash
uvicorn main:app --reload
```

### 3. Acces la documentație
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Utilizare

### Autentificare

**User default:**
- Username: `admin`
- Password: `admin123`

### 1. Înregistrare user nou
```bash
POST /auth/register
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

### 2. Login
```bash
POST /auth/login
{
  "username": "john",
  "password": "password123"
}
```

Răspuns:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer"
}
```

### 3. Folosire token
Adaugă header-ul în toate request-urile protejate:
```
Authorization: Bearer <access_token>
```

## Endpoint-uri API

### Autentificare
- `POST /auth/register` - Înregistrare user nou
- `POST /auth/login` - Login user

### Useri (necesită autentificare)
- `GET /users/me` - Informații user curent
- `GET /users/` - Lista tuturor userilor
- `GET /users/{user_id}` - User specific
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Șterge user

## Arhitectura

```
app/
├── core/           # Configurări, securitate, excepții
├── domain/         # Business logic (entities, services, repositories)
├── infrastructure/ # Implementări concrete (database, repositories)
└── presentation/   # API layer (schemas, routers, dependencies)
```

### Domain Layer
- **Entities**: Modele de business pure
- **Services**: Logica de business
- **Repositories**: Interfețe pentru accesul la date

### Infrastructure Layer
- **Database**: Mock database (în memorie)
- **Repositories**: Implementări concrete

### Presentation Layer
- **Schemas**: Modele pentru API requests/responses
- **Routers**: Endpoint-urile API
- **Dependencies**: Dependency injection

## Teste

Rulare teste:
```bash
pytest tests/ -v
```

## Următorii Pași

1. **Docker**: Containerizare aplicație
2. **PostgreSQL**: Înlocuire mock database cu PostgreSQL
3. **Migrations**: Alembic pentru migrații
4. **Logging**: Sistem de logging
5. **Rate limiting**: Protecție împotriva spam-ului

## Structura pentru Lecția Următoare

Aplicația este pregătită pentru:
- Adăugare Docker Compose
- Conectare la PostgreSQL
- Demonstrarea diferenței între mock și database real
- Explicarea containerelor și orchestrării