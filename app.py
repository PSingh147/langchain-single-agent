import streamlit as st
from main import get_weather

st.set_page_config(page_title="Weather Agent", page_icon="⛅", layout="centered")

st.title("🌦️ AI Weather Agent (Using LangChain)")
st.write("Ask about the weather in any city.")

# -----------------------------
# User Input
# -----------------------------

user_query = st.text_input(
    "Enter your weather question:",
    "What's the weather in the capital of USA?"
)

if st.button("Get Weather"):
    with st.spinner("Fetching weather..."):
        result = get_weather(user_query)

        if "error" in result:
            st.error(result["error"])
        else:
            structured = result["structured"]
            raw = result["raw"]

            # -----------------------------
            # Main Weather Output
            # -----------------------------


            st.subheader("Weather Result")
            st.write(f"**City:** {result.get('city', 'N/A')}")
            st.write(f"**Temperature (°C):** {result.get('temparature_celcius', 'N/A')}")

            # -----------------------------
            # Sidebar: Raw Tavily Results
            # -----------------------------
            st.sidebar.header("🔍 Raw Tavily Search Output")

            if raw:
                st.sidebar.json(raw)
            else:
                st.sidebar.write("No raw Tavily results found.")