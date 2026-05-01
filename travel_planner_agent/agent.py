# from google.adk.agents.llm_agent import Agent
# from datetime import datetime

# def now() -> dict:
#     """Returns the current date and time."""
#     my_datetime = ... # Ask Gemini CLI to help you!
#     return {
#         "status": "success",
#         "current_time": my_datetime
#     }

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
#     tools=[now] # <== This is the only line you want to add.
# )
# from google.adk.agents import Agent
# from datetime import datetime

# def now() -> dict:
#     """Returns the current date and time."""
#     my_datetime = datetime.now()
#     return {
#         "status": "success",
#         "current_time": my_datetime
#     }
# root_agent = Agent(
#     name="travel_basic",
#     model="gemini-2.5-flash",
#     instruction="You are a helpful travel assistant." +
#     "You can help with general travel advice based on your knowledge.",
#     tools=[now]
# )
# from google.adk.agents import Agent
# from google.adk.tools import google_search

# root_agent = Agent(
#     name="travel_agent",
#     model="gemini-2.5-flash",
#     tools=[google_search],
#     instruction="""You are a travel agent.
# Your job is to help the user plan a trip.
# You have access to a search engine.
# If you don't know the answer, you can use the search engine.
# When you are done, reply with "DONE".""",
# )
from google.adk.agents.llm_agent import Agent
from travel_agent import travel_agent
from weather_agent import weather_agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Main router agent that sends tasks to sub-agents.",
    instruction="""
You are the main assistant.

Route user requests:

- If user asks about travel, trips, flights → use travel_agent
- If user asks about weather, temperature, forecast → use weather_agent

If unsure, respond directly.
""",
    sub_agents=[travel_agent, weather_agent]
)