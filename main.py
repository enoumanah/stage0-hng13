from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
from datetime import datetime, timezone

app = FastAPI(title="HNG13 - Stage 0")

CAT_FACT_URL = "https://catfact.ninja/fact"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/me", response_class=JSONResponse)
async def get_me():
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(CAT_FACT_URL)
            response.raise_for_status()
            fact_data = response.json()
            cat_fact = fact_data.get("fact", "Cats are awesome!")
    except httpx.RequestError:
        cat_fact = "could not fetch a cat fact at this time."
    except httpx.HTTPStatusError:
        cat_fact = "external service error."

    response_data = {
        "status": "success",
        "user": {
            "email": "umanaheno10@gmail.com",
            "name": "Eno Umanah",
            "stack": ["Python", "FastAPI"],
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact,
    }

    return JSONResponse(content=response_data)