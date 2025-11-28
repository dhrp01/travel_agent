import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

accommodations_agent = Agent(
    name="accommodations_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="An accommodations recommendation agent that can suggest places to stay.",
    instruction="""
    You are an accommodations recommendation assistant.
    Given a location, your task is to list out top accommodations to stay as a tourist.
    Use Google Search to find popular accommodations if unsure.

    # Rules:
    - Find accommodations that are highly rated and well-reviewed.
    - Find accommodations that are conveniently located near major attractions.
    - Provide which accommodation is closest to which attraction.
    - Suggest a mix of accommodation types (hotels, hostels, vacation rentals).
    """,
    tools=[google_search],
)
