import json
import csv
import logging

# logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
def process_student():
    try :
        logging.info("Program Started")

# Step 1: Read JSON
        with open("student.json","r") as f:
            students = json.load(f)

        logging.info("Json file loaded successfully")


# Step 2: Filter pass students
# pass_student = [s for s in students if s["marks"] >= 50]

# Step 3: Prepare CSV data
        final_data = [
            {"name" : s["name"],
            "status":"Pass" if s["marks"] >= 50 else "Fail"}
            for s in students
    ]

# Step 4: Write CSV
        with open("result.csv",'w',newline="") as f:
            writer = csv.DictWriter(f,fieldnames=["name","status"])
            writer.writeheader()
            writer.writerows(final_data)

        logging.info("CSV Files written Successfully")

    except FileNotFoundError:
        logging.error("Student Json file not found")

    except json.JSONDecodeError:
        logging.error("Invalid Json Format")

    except Exception as e:
        logging.error(f"Unexpected Error : {e}")

    else :
        logging.info("Program Complete Without Error")

    finally:
        logging.info("Program Ended")

process_student()
