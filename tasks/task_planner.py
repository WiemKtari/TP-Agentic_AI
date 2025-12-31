from crewai import Task
from agents.planner import planner_agent

task_planner = Task(
    description="""
Create a complete data science project plan for the topic: {topic}.

Rules:
- Do NOT ask questions
- Assume the business problem is already defined
- Focus on execution steps

Steps:
1. Define the problem and objectives
2. Describe data understanding and preparation steps
3. Outline modeling and evaluation steps
4. Include deployment or reporting considerations

Output:
- A clear step-by-step project plan
""",
    expected_output="Structured data science project plan",
    agent=planner_agent
)
