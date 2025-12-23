import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


async def analyze_sector(sector: str, market_data: str) -> str:
    """
    Uses Gemini API to generate a markdown market analysis report
    for the given Indian market sector.
    """

    prompt = f"""
You are a professional market analyst.

Generate a detailed **Markdown report** for the Indian **{sector}** sector.

The report MUST contain:

# {sector.title()} Sector Trade Opportunities (India)

## Market Overview
## Current Market Trends
## Key Trade Opportunities
## Risks & Challenges
## Short-term Outlook

Use the following market information for analysis:

{market_data}
"""

    response = model.generate_content(prompt)
    return response.text
