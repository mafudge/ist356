import pandas as pd
import requests

import requests
response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")
employees = response.json()

departments = []
for dept_name in employees.keys():
    dept_employees = pd.json_normalize(employees,  record_path=dept_name)
    dept_employees['dept'] = dept_name
    departments.append(dept_employees)

combined = pd.concat(departments, ignore_index=True)
print(combined)