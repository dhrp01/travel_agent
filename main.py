import asyncio
from agents.agent import travel_agent

async def main():
    print(f"Hello from travel-agent!")
    response = await travel_agent("Paris")
    print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())
    