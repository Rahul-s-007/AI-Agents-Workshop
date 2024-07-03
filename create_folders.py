import os

# List of folders to create
folders = ["Actions", "Helpers"]

# List of files to create
files = [
    ".env",
    ".gitignore",
    "logs.txt",
    "main_agent.py",
    "Prompts.py",
    "requirements.txt",
    "Tools.py"
]

# Create folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Create files
for file in files:
    with open(file, 'w') as f:
        pass  # to create an empty file

print("Folders and files created successfully.")
