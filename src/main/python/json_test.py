import json

dir_obj = {
    "name" : "Vivek",
    "LName": "Khandelwal",
    "Phone": {"Airtel": "9909993807", "Jio": "8618101576"},
    "Stays": ["Kirkend", "Dhanbad", "Kolkatta1", "Surat", "Pali", "Jodhpur", "Balotra", "Jasol", "Bangalore", "Pune", "Mumbai", "Kinshasa"],
    "Age"  : "38"
}

json_obj = json.dumps(dir_obj, indent=4)
with open("/data/test.json", "w") as outfile:
    outfile.write(json_obj)