import json
fileLocation = 'food.json'
with open(fileLocation,'w+',encoding = 'utf-8') as f:
    f.writelines("[")
    for i in range(1,6):
        print("Nhap combo %d: "%i)
        c = input()
        f.writelines(c)
        if i < 5:
            f.writelines(",")
    f.writelines("]")

with open("food.json", "r") as read_file:
    file = json.load(read_file)
 
print(file)
