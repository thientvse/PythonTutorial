print("In ra tong 100 so dau tien dung while")

tong = 0
i = 1
while i < 100:
    tong = tong + i
    i += 1

print("Ket qua:"+str(tong))


print("In ra nhung so chia het cho 3 trong khoang 20-50")

i = 20
tong = 0
while i < 50:
    if i%3 == 0 :
        print(str(i)+" ")
    i += 1
