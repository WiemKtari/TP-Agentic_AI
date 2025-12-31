from crewai import Agent
from tools.csv_reader import CSVReaderTool
from tools.data_stats import DataStatsTool
from llm_config import OLLAMA_LLM

analyst_agent = Agent(
    role="Data Analyst",
    goal="Perform exploratory data analysis",
    backstory="Expert in EDA and statistics",
    tools=[CSVReaderTool(), DataStatsTool()],
    llm=OLLAMA_LLM,
    verbose=True
)
