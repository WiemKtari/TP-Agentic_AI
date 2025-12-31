from crewai import Task
from agents.writer import writer_agent

task_report = Task(
    description="""
Write a final technical report in Markdown format summarizing the entire project.

Inputs available:
- Project plan
- EDA summary
- Modeling proposal

Rules:
- Write in a professional and academic tone
- Do NOT invent results
- Structure the report clearly

Report structure:
1. Introduction
2. Problem Statement
3. Data Exploration Summary
4. Modeling Strategy
5. Conclusion and Next Steps

Output:
- A clean and well-formatted Markdown report
""",
    expected_output="Final markdown report",
    agent=writer_agent
)
