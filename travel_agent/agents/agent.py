import os
from dotenv import load_dotenv
import random

from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types
import vertexai
from vertexai import agent_engines

from agents.attractions import attractions_agent
from agents.accomodations import accommodations_agent
from agents.restraurants import restaurants_agent
from agents.travel_essentials import travel_essentials_agent


load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
vertexai.init(
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ["GOOGLE_CLOUD_LOCATION"],
)

parallel_agent = ParallelAgent(
    name = "travel_agents_parallel",
    sub_agents=[
        accommodations_agent,
        restaurants_agent,
        travel_essentials_agent,
        ],
)

root_agent = SequentialAgent(
    name = "travel_agents",
    sub_agents=[
        attractions_agent,
        parallel_agent,
    ],
)

regions_list = ["europe-west1", "europe-west4", "us-east4", "us-west1"]
deployed_region = random.choice(regions_list)

print(f"Selected deployment region: {deployed_region}")