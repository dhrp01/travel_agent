import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.adk.tools.function_tool import FunctionTool

from ..tools.userInput import get_user_input
from ..tools.googleSearchAgentTool import search_tool

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

travel_essentials_agent = Agent(
    name="travel_essentials_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="A travel essentials recommendation agent that suggests what to pack according to the destination and weather.",
    instruction="""
    You are a travel essentials recommendation assistant.
    Given a location, your task is to list out essential items to pack for a tourist.
    Use Google Search to find popular travel essentials if unsure.
    To get the specific travel month from the user, ask them directly if not provided.

    # Rules:
    - Recommend essential items based on the destination and weather.
    - Consider different types of travelers (e.g., business, leisure, adventure).
    - Suggest items for various weather conditions (e.g., rain, cold, heat).
    - Include any travel safety and health essentials.
    """,
    tools=[get_user_input, search_tool],
)
