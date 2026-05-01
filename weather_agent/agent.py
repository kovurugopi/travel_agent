from google.adk.agents.llm_agent import Agent

weather_agent = Agent(
    model="gemini-2.5-flash",
    name="weather_agent",
    description="Provides weather information and forecasts.",
    instruction="""
You are a weather assistant.

Help users with:
- Current weather
- Forecasts
- Best time to travel based on weather
- Packing suggestions

Keep answers short and practical.
"""
)