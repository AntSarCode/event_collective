# Event Collective

**Event Collective** is a full-stack web application built to manage professional event coordination, digital media galleries, customer engagement, and service bookings. The platform combines PostgreSQL, FastAPI, and modern React-based frontend tooling.

---

## 🛠️ Tech Stack

**Backend:**
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Alembic (migrations)
- Pydantic (schemas)

**Frontend:** *(in development)*
- React + Vite
- TypeScript
- Tailwind CSS

**Infrastructure:**
- Dockerized local development
- GitHub for source control

---

## 📂 Project Structure

```
/event_collective
│
├── app/                 # FastAPI application
│   ├── api/             # Route declarations and dependency injections
│   ├── config/          # Settings and environment variables
│   ├── core/            # Application startup, auth, and security logic
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic and DB interactions
│   └── utils/           # Helper utilities
│
├── tests/               # Unit and integration tests
├── scripts/             # SQL and data seeding scripts
├── main.py              # FastAPI entry point
├── requirements.txt     # Python dependencies
└── README.md            # Project overview
```

---

## 🚀 Features

- User authentication with admin role support
- Gallery and service management
- Review and rating system
- Relational PostgreSQL schema with triggers & indexes
- API-ready backend for React integration

---

## 🔐 Security Practices

- Password hashing (bcrypt)
- Role-based access control
- JWT-based session management

---

## 🚧 Setup Instructions (Local Dev)

```bash
# 1. Clone repo
$ git clone https://github.com/your-org/event-collective.git

# 2. Navigate to project
$ cd event-collective

# 3. Create virtual environment and activate it
$ python -m venv .venv
$ source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 4. Install dependencies
$ pip install -r requirements.txt

# 5. Set environment variables (create .env file)
# Example:
DATABASE_URL=postgresql://user:pass@localhost:5432/event_collective

# 6. Run the app
$ uvicorn main:app --reload
```

---

## 📌 Roadmap

- [✅] Backend scaffold + schema
- [✅] Triggers, indexes, and optimized SQL
- [⏳] Frontend development (React/Vite)
- [⏳] Admin dashboard UI
- [⏳] Deployment to production (Docker, Fly.io or Render)

---

## 🤝 License+

MIT License © 2025 Event Collective Development Team
