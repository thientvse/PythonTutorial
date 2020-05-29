listSeaFood = ["ca", "tom", "cua", "tom hum", "cua alaska","oc huong"]
fileLocation = 'seafood.csv'
with open(fileLocation,'w',encoding = 'utf-8') as f:
    f.write("ten")
    f.writelines("\n")
    for seafood in listSeaFood:
        f.writelines(seafood)
        f.writelines("\n")

f = open(fileLocation, 'r', encoding='utf-8')

print(f.read())