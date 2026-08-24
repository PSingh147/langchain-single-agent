import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent, AgentState
from langchain.agents.structured_output import ProviderStrategy

from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Define Schema
# -----------------------------

weather_info_schema = {
    "title" : "Weather Information",
    #"type" : "object",
    "description": "Weather information for a city.\n",
    "properties":{
        "city" : {"type":"string", "description":"The name of the city"},
        "temparature_celcius" : {"type":"string", "description":"Temarature of the city"}   
    },

    "required": ["city", "temparature_celcius"]
}

# -----------------------------
# Tools & Model Setup
# -----------------------------

search_tool = TavilySearch(max_results =1)               
tool_list = [search_tool]

model = ChatGoogleGenerativeAI(
    model= "gemini-3.7-flash",
    temperature=0.5,
    api_key=GEMINI_API_KEY
)

agent = create_agent(
    model= model,
    tools = [search_tool],
    response_format=ProviderStrategy(weather_info_schema)
    )

# -----------------------------
# Public function for Streamlit
# -----------------------------


def get_weather(query: str):
    """
    Runs the weather agent and returns:
    - structured weather info
    - raw Tavily tool output (for sidebar)
    """
    try:
        input_payload = {
            "messages": [{"role": "user", "content": query}]
        }

        response = agent.invoke(input_payload)

        structured = response.get("structured_response", {})
        raw_tool_output = None

        # Extract raw Tavily results from intermediate steps
        if "intermediate_steps" in response:
            steps = response["intermediate_steps"]
            if steps and len(steps) > 0:
                # Each step is (tool_call, tool_result)
                _, tool_result = steps[0]
                raw_tool_output = tool_result

        return {
            "structured": structured,
            "raw": raw_tool_output
        }

    except Exception as e:
        return {"error": str(e)}





