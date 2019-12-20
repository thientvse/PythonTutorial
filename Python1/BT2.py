import math

print("Hinh chu nhat")
a = int(input("Nhap chieu dai: "))
b = int(input("Nhap chieu rong: "))

print("Chieu dai: " + str(a) + " Chieu rong: " + str(b))

print("\nChu vi hinh chu nhat: " + str((a + b) * 2))
print("\nDien tich hinh chu nhat: " + str(a * b))

print("\nHinh tam giac")
c = int(input("Nhap canh 1: "))
d = int(input("Nhap canh 2: "))
e = int(input("Nhap canh 3: "))

print("Canh 1: " + str(c) + " Canh 2: " + str(d) + " Canh 3: " + str(e))

print("\nChu vi hinh tam giac: " + str(c + d + e))
p = (c + d + e) / 2
print("\nDien tich hinh tam giac: " + str(math.sqrt(p * (p - c) * (p - e) * (p - d))))

print("\nHinh Tron")
r = int(input("Nhap ban kinh: "))

print("\nChu vi hinh tron: " + str(2 * r * math.pi))
print("\nDien tich hinh tron: " + str(r * r * math.pi))
