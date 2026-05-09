from google.adk.agents.llm_agent import Agent
from .travel_agent.agent import travel_agent
from .weather_agent.agent import weather_agent
from datetime import datetime

def now() -> dict:
    """Returns the current date and time."""
    my_datetime = datetime.now()
    return {
        "status": "success",
        "current_time": str(my_datetime)
    }

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Main router agent that sends tasks to sub-agents.",
    tools=[now,],
    instruction="""
You are the main assistant.

Route user requests:

- If user asks about travel, trips, flights → use travel_agent
- If user asks about weather, temperature, forecast → use weather_agent

If unsure, respond directly.
""",
    sub_agents=[travel_agent, weather_agent]
)