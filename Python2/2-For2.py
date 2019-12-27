print("In ra tong cac so nguyen trong khoang 200-600 va chia het cho 3")

tong = 0
for i in range (200,600):
    if i%3 == 0 :
        tong = tong + i

print("Ket qua: "+str(tong))


print("In ra tong cac so nguyen trong khoang 50-100 va chia het cho 5")

tong = 0
for i in range (50,100):
    if i%5 == 0 :
        tong = tong + i

print("Ket qua: "+str(tong))
