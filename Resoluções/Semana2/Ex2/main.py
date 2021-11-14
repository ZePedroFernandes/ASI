import json

array = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]

freq = {}
for value in array:
    if value not in freq.keys():
        freq[value] = array.count(value)

print(json.dumps(freq, indent=2))
