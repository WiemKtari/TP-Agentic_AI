from crewai import Task
from agents.modeller import modeller_agent

task_model = Task(
    description="""
Based on the EDA results, propose baseline machine learning models for the problem described in {topic}.

Rules:
- Do NOT train models
- Do NOT write code
- Focus on reasoning and justification

Steps:
1. Identify the type of problem (classification or regression)
2. Propose at least 2 baseline models
3. Justify model choices based on data characteristics
4. Propose suitable evaluation metrics

Output:
- A structured modeling proposal
""",
    expected_output="Baseline models and evaluation metrics proposal",
    agent=modeller_agent
)
