from crewai import Agent
from llm_config import OLLAMA_LLM


writer_agent = Agent(
    role="Report Writer",
    goal="Write a coherent technical report",
    backstory="Technical data science writer",
    llm=OLLAMA_LLM,
    tools=[],
    verbose=True
)
