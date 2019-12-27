print("tinh tong va tong binh phuong 100 so dau tien")

tong = 0
for i in range(1,100):
    tong = tong + i

print("Tong 100 so dau tien: "+str(tong))

tongSquare = 0
for i in range(1,100):
    tongSquare = tongSquare + i*i
print("Tong 100 so dau tien: "+str(tongSquare))


print("Trung binh cong 100 so dau tien: "+str(tong/100))

a = int(input("Nhap so bat ky: "))

giaithua = 1
for i in range (1, a+1):
    giaithua = giaithua*i

print("Giai thua cua "+str(a)+": " + str(giaithua))