print("Nhap duong dan file data.txt:")
fileLocation = input()
print("Duong dan ban nhap:",fileLocation)

with open(fileLocation,'w',encoding = 'utf-8') as f:
    for i in range(5):
        print("Nhap ten trai cay %d :" %(i+1))
        fruit = input()
        f.writelines(fruit)
        f.writelines("\n")

f = open(fileLocation, 'r', encoding='utf-8')

print(f.read())


