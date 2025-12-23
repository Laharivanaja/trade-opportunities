# Trade Opportunities API

## Project Overview
The Trade Opportunities API is a FastAPI-based backend service that analyzes current Indian market sectors and provides AI-generated trade opportunity insights.

The API accepts a sector name (for example: pharmaceuticals, technology, agriculture), gathers relevant market context, and generates a structured Markdown market analysis report using the Google Gemini LLM.

---

## Features
- Single REST endpoint for sector-based market analysis
- AI-powered insights using Google Gemini
- Markdown-formatted trade analysis reports
- JWT-based authentication
- Rate limiting to prevent abuse
- In-memory session tracking (no database)
- Graceful error handling
- Auto-generated API documentation (Swagger UI)

---

## Technology Stack
- Backend Framework: FastAPI  
- AI Model: Google Gemini API  
- HTTP Client: httpx  
- Authentication: JWT  
- Rate Limiting: SlowAPI  
- Storage: In-memory (Python dictionaries)

---

## Project Structure
trade-opportunities/
│── app/
│ ├── main.py # FastAPI entry point
│ ├── auth.py # JWT authentication
│ ├── rate_limiter.py # Rate limiting logic
│ ├── session.py # In-memory session tracking
│ ├── models.py # Pydantic models
│ ├── utils.py # Helper utilities
│ └── services/
│ ├── ai_service.py # Gemini AI integration
│ └── search_service.py# Market data collection
│
├── README.md
├── requirements.txt
└── .env 

## Setup Instructions

### 1. Clone the Repository
git clone (https://github.com/Laharivanaja/trade-opportunities.git)
cd trade-opportunities 

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate # Windows

### 3. Install Dependencies
python -m pip install -r requirements.txt

## Environment Configuration
Create a `.env` file in the root directory and add:

GEMINI_API_KEY=AIzaSyCsQEdhN2977TJB2RcMgTK3rqeZ8V0toKg
JWT_SECRET=trade_opportunities_secret


## Authentication (JWT)
Generate a JWT token using Python shell:

python

from app.auth import create_access_token
print(create_access_token("test_user"))

Use the generated token in API requests:

Authorization: Bearer <your_jwt_token>

## Running the Application
Start the FastAPI server:

python -m uvicorn app.main:app --reload


The server will be available at:

http://127.0.0.1:8000


## API Documentation
Swagger UI is available at:

http://127.0.0.1:8000/docs

## API Endpoint

### GET /analyze/{sector}

#### Example Request
GET /analyze/pharmaceuticals



#### Headers
Authorization: Bearer <JWT_TOKEN>

#### Example Response
{
"sector": "pharmaceuticals",
"analysis_markdown": "# Pharmaceuticals Sector Trade Opportunities (India)\n\n## Market Overview\n..."
}


The response contains a Markdown-formatted trade analysis report that can be saved as a `.md` file.

---

## Security Measures
- JWT-based authentication
- Rate limiting (5 requests per minute per user)
- Input validation
- In-memory session tracking
- Error handling for external service failures

---

## Evaluation Criteria Coverage

| Requirement | Status |
|------------|--------|
FastAPI Implementation | Completed |
AI Integration (Gemini) | Completed |
Market Data Collection | Completed |
Authentication & Security | Completed |
Rate Limiting | Completed |
Markdown Report Output | Completed |
Clean Architecture | Completed |
Error Handling | Completed |

---

## Notes
- No database is used (in-memory storage only)
- API keys must not be committed to version control
- Designed for academic and evaluation purposes

---

## Conclusion
This project demonstrates a real-world FastAPI backend application integrating AI-powered analysis, security mechanisms, rate limiting, and clean architecture to deliver structured trade opportunity insights for Indian market sectors.

