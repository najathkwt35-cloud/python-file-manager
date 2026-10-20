
from pathlib import Path

# Find your Documents folder automatically
documents = Path.home() / "Documents"

# Main folder
main_folder = documents / "CSE_HND"

# Subfolders to create
folders = [
    "01_Programming",
    "02_Database_Management",
    "03_Computer_Networks",
    "04_Software_Engineering",
    "05_Boolean_Algebra",
    "06_Assignments",
    "07_Projects",
    "08_Lecture_Notes",
    "09_Exam_Papers",
    "10_Certificates"
]

# Create the main folder
main_folder.mkdir(parents=True, exist_ok=True)

# Create all subfolders
for folder in folders:
    folder_path = main_folder / folder
    folder_path.mkdir(exist_ok=True)

print("CSE HND folders created successfully!")

print(f"\nLocation: {main_folder}")

for folder in folders:
    print(f"[OK] {folder}")
