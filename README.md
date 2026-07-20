# TPP // ThePeerProject Backend
<img width="4500" height="1500" alt="image" src="https://github.com/user-attachments/assets/5f312f0d-c57a-4a75-ad7f-6d01ff490f30" />

> free // student-run // non-profit in collaboration of r/CBSE, r/ICSE, and r/JEE

> https://peerproject.in

## Overview
PeerProject is a student-focused mentorship platform designed to connect current high schoolers with the high school grads who walked the same path as they did. 

The Backend provides secure authentication, mentor/mentee management, AI-assisted mentor-mentee assignment and API endpoints for frontend and discord bot integration. 

## Architecture
<img width="1556" height="928" alt="image" src="https://github.com/user-attachments/assets/0ea517a5-ade0-4563-8d5b-7bb2e8c11d47" />
The Architecture choosen is the hub-spoke for easy upgradability. 

## Features
- JWT Authentication
- PostgreSQL Database with Supabase
- AI-powered Mentor-Mentee Assignment(will be available in V2)
- GraphQL Integration(Will be available in V2)
- Embeddings using pgvector in supabase.
- Mentor/Mentee Registration
- Secure API Calls
- Rest API

## Tech Stack
Backend
- FastAPI
- Python
- Pydantic for validation

Database
- PostgreSQL
- Supabase

Authentication
- JWT
- bcrypt

AI/LLM Services
- HuggingFace
- NVIDIA Llama Nemotron Embed 1B V2
- Gemma for assignment
- Deepseek for profile analysis

Deployment(planned)
- Docker

## Installation
```bash
git clone github.com/ShyZen15/The-Peer-Project-Backend
cd The-Peer-Project-Backend
python -m venv .venv
pip install -r requirements.txt
```

## File Structure
```
The-Peer-Project-Backend/
|
├── App/
    ├── AI/
    ├── api/
    ├── auth/
    ├── repository/
    ├── schemas/
    ├── services/
    ├── config.py
    ├── main.py
    └── test.py
├── .gitignore
├── database.py
└── requirements.txt
```

## Environment Variables
Refer to .env.example under App/

## Running
```bash
fastapi dev
```

## API Documentation
FastAPI uses Swagger UI in its docs for testing API endpoints
hence to access it go to https://localhost:8000/docs

## Database Design
<img width="982" height="988" alt="image" src="https://github.com/user-attachments/assets/eedea6ef-ddc2-42f8-b269-529245d0f890" />

## Roadmap

- [x] Mentor APIs
- [x] Mentee APIs
- [x] Admin Authentication
- [x] AI Embeddings
- [x] Semantic Search
- [ ] Mentor Assignment Engine
- [ ] GraphQL API
- [ ] Discord Bot Integration
- [ ] Docker Deployment
- [ ] CI/CD Pipeline

## Author
Developed by Shiven Sharma(ShyZen15) Co-Founder @ ThePeerProject

## Copyright
© 2026 peerproject.in. all rights reserved. 

