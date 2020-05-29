import json
with open("food.json", "r") as read_file:
    jsonData = json.load(read_file)
 
print(jsonData)
sorted_string = json.dumps(jsonData, indent=4, sort_keys=True)
print(sorted_string)

with open("food.json", "r") as read_file:
    jsonData = json.load(read_file)
    jsonData['combo1'] = "chao long, tiet canh, ruou"

with open('food.json', 'w') as f:
    f.write(json.dumps(jsonData))


with open("food.json", "r") as read_file:
    jsonData = json.load(read_file)
 
print(jsonData)