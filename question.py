
import json


with open("data.json", "r") as f:
    data = json.load(f)
print(f"Привіт, {data['name']}! Тобі {data['age']} років.")