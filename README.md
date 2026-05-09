# Travel Planner Agent

A multi-agent travel assistant built with Google's Agent Development Kit (ADK) and Gemini 2.5 Flash. The system uses a router architecture to delegate tasks to specialized sub-agents.

## Architecture

```
root_agent (Router)
├── travel_agent — Trip planning, flights, hotels, itineraries
└── weather_agent — Current weather, forecasts, packing suggestions
```

- **Root Agent** — Routes user requests to the appropriate sub-agent based on intent.
- **Travel Agent** — Handles travel planning including flight suggestions, hotel recommendations, and daily itineraries.
- **Weather Agent** — Provides weather information using the Open-Meteo API and Google Search.

## Project Structure

```
travel_planner_agent/
├── __init__.py
├── agent.py                  # Root agent with routing logic
├── travel_agent/
│   ├── __init__.py
│   └── agent.py              # Travel planning sub-agent
└── weather_agent/
    ├── __init__.py
    └── agent.py              # Weather sub-agent with tools
```

## Prerequisites

- Python 3.12+
- Google ADK (`google-adk`)
- A valid Google API key (Gemini)

## Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd GoogleDevCamp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install google-adk
   ```

4. Create a `.env` file in the project root with your API key:
   ```
   GOOGLE_API_KEY=your-api-key-here
   ```

## Running the Agent

```bash
adk run travel_planner_agent
```

Or use the ADK web interface:

```bash
adk web
```

## Usage Examples

- "Plan a 3-day trip to Paris"
- "What's the weather like in London?"
- "Suggest hotels in New York for next weekend"
- "Should I pack a jacket for my trip to Paris?"

## Supported Weather Cities

The weather tool currently supports:
- London
- Paris
- New York

## License

This project is for educational purposes as part of Google Dev Camp.
