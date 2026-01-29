import json
import csv

# Step 1: Read JSON
with open("student.json","r") as f:
    students = json.load(f)

# Step 2: Filter pass students
pass_student = [s for s in students if s["marks"] >= 50]

# Step 3: Prepare CSV data
final_data = [{"name" : s["name"],"status":"Pass"} for s in pass_student]

# Step 4: Write CSV
with open("result.csv",'w',newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["name","status"])
    writer.writeheader()
    writer.writerows(final_data)
