print("Kiem tra chan le\n")

number = int(input("Nhap so bat ky: "))

number = number % 2
if number == 0:
    print("So chan")
elif number == 1:
    print("So le")

print("\nNhap 3 so")
a = float(input("Nhap so 1: "))
b = float(input("Nhap so 2: "))
c = float(input("Nhap so 3: "))

print("\nTong 3 so: "+str(a+b+c))


