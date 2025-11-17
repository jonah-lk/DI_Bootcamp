import json, os

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "2000-10-09"

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "modified.json")
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)