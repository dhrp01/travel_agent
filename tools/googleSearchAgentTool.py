from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

search_agent = Agent(
    name="travel_search_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    description="Agent that uses Google Search for travel information.",
    instruction="""
    You are a search specialist for travel.
    Use Google Search to find current and accurate information about
    destination's weather, and travel requirements.
    """,
    tools=[google_search],
)

search_tool = AgentTool(agent=search_agent)
