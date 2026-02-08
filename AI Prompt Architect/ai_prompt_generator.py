import random

roles = [
    "Software Engineer",
    "Data Scientist",
    "Content Writer",
    "UX Designer",
    "Project Manager",
    "Marketing Specialist"
]

tasks = [
    "analyze and debug code",
    "create a data visualization",
    "write a blog post",
    "design a user interface",
    "plan and organize tasks",
    "develop a marketing strategy"
]

formats = [
    "JSON",
    "Markdown",
    "HTML",
    "CSV",
    "Python code",
    "Plain text"
]

role = random.choice(roles)
task = random.choice(tasks)
format_type = random.choice(formats)

print(f"Act as a {role}. Your task is to {task}. Output format: {format_type}.")
