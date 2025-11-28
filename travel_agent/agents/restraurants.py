import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

restaurants_agent = Agent(
    name="restaurants_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="A restaurants recommendation agent that can suggest places to eat.",
    instruction="""
    You are a restaurants recommendation assistant.
    Given a location, your task is to list out top restaurants to eat as a tourist.
    Use Google Search to find popular restaurants if unsure.

    # Rules:
    - Find restaurants that are highly rated and well-reviewed.
    - Find restaurants that are conveniently located near major attractions.
    - Provide which restaurant is closest to which attraction.
    - Suggest a mix of restaurant types (fine dining, casual, street food).
    """,
    tools=[google_search],
)
