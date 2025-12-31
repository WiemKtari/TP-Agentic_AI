from crewai import Agent
from llm_config import OLLAMA_LLM

planner_agent = Agent(
    role="Project Planner",
    goal="Create a structured data science plan",
    backstory="Senior data science project manager",
    llm=OLLAMA_LLM,
    tools=[],
    verbose=True
)
