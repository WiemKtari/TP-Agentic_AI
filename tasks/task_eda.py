from crewai import Task
from agents.analyst import analyst_agent

task_eda = Task(
    description="""
Perform exploratory data analysis (EDA) on the dataset provided in {csv_path}.

Rules:
- Use the CSV file exactly at {csv_path}
- Do NOT invent any other file paths
- Use csv_reader to inspect the data
- Use data_stats to compute statistics
""",
    expected_output="Clear EDA summary with statistics and insights",
    agent=analyst_agent
)
