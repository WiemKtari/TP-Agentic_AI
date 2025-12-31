from crewai import Agent
from llm_config import OLLAMA_LLM


modeller_agent = Agent(
    role="Modelling Agent",
    goal="Propose baseline ML models",
    backstory="ML engineer specialized in baselines",
    llm=OLLAMA_LLM,
    tools=[],
    verbose=True
)
