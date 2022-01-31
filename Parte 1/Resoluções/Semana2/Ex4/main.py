import json

table = {
    "filme": ["film","movie"],
    "locomotiva": ["locomotive", "train"],
    "pessoa": ["person", "individual"]
}

print(json.dumps(table, indent=2))

print(table["locomotiva"])