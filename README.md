# 🐱 HNG13 – Stage 0: Profile API (FastAPI)

Welcome to **Stage 0** of the **HNG13 Backend Track**!  
This simple FastAPI project implements a RESTful endpoint `/me` that returns your personal profile information and a dynamic **random cat fact** fetched from an external API.

---

## 🚀 Project Overview

### 🎯 Objective
Build a REST API endpoint that demonstrates:
- JSON response formatting  
- External API integration  
- Dynamic data (current UTC timestamp & cat facts)  
- Error handling and clean FastAPI design  

### 🧩 Endpoint Summary
| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/me` | Returns your profile info + random cat fact |

---

## 📦 Project Structure

stage0-hng13/
│
├── main.py # Main FastAPI application
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/stage0-hng13.git
cd stage0-hng13
```

### 2. Create and Activate a Virtual Environment

python -m venv venv
# Activate
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies

pip install fastapi uvicorn httpx

### 4. Run the API Locally

uvicorn main:app --reload

Your app will be running at:
👉 http://127.0.0.1:8000/me

### 🧠 Implementation Details
🐾 External API

Cat Facts API: https://catfact.ninja/fact

Used to fetch a random cat fact dynamically on every request.

###🧰 Tools & Libraries
Library & Purpose
FastAPI	Framework for building the RESTful API
HTTPX	Async HTTP client for calling external APIs
Uvicorn	ASGI server to run FastAPI apps

### 🔍 Example Response

Endpoint: GET /me

{
  "status": "success",
  "user": {
    "email": "umanaheno10@gmail.com",
    "name": "Eno Umanah",
    "stack": ["Python", "FastAPI"]
  },
  "timestamp": "2025-10-16T09:12:34.567890+00:00",
  "fact": "Cats sleep for 70% of their lives."
}

### 🧩 Code Explanation
/me Endpoint Logic

Fetch cat fact from the external API

Handle errors gracefully (e.g., API down or timeout)

Build response JSON including:

status: Always "success"

user: Your profile info

timestamp: Current UTC time in ISO 8601 format

fact: The fetched cat fact

Return JSON response with proper content type

### 🧱 Error Handling

If the external API fails or times out:

A fallback message like "could not fetch a cat fact at this time." is returned instead of breaking the app.

### 🧭 Additional Features

CORS middleware enabled for cross-origin requests

Dynamic UTC timestamps updated on each request

Clean async HTTP calls using httpx.AsyncClient

JSONResponse used to ensure application/json content type
