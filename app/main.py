from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.rate_limiter import limiter
from app.auth import verify_token
from app.services.search_service import fetch_market_news
from app.services.ai_service import analyze_sector
from app.session import track_session

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyzes Indian market sectors and provides trade insights",
    version="1.0"
)

# Rate limiting setup
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze(
    request: Request,          # ✅ REQUIRED by SlowAPI
    sector: str,
    user=Depends(verify_token)
):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Sector must contain only letters")

    track_session(user["user_id"])

    try:
        market_data = await fetch_market_news(sector)
        report = await analyze_sector(sector, market_data)

        return {
            "sector": sector,
            "analysis_markdown": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
