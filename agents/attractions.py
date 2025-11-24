import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

attractions_agent = Agent(
    name="attractions_list_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="An attractions recommendation agent that can suggest places to visit.",
    instruction="""
    You are an attractions recommendation assistant.
    Given a location, your task is to list out top attractions to visit as a tourist.
    Use Google Search to find popular attractions if unsure.

    # Rules:
    - Club all attractions that can be visited together in one day.
    - Provide a brief description (1–2 sentences) for each attraction.
    - Suggest the best time to visit each attraction.
    - If the location is not well-known, use Google Search to find relevant attractions.
    - Arrange the attractions so that must-visit places are listed first.
    - At the end, provide list of all attractions in bullet points for easy reference,
      under the heading "### List of Attractions".
    """,
    tools=[google_search],
)
