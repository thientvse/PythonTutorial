print("Chon chuc nang muon thuc hien")
print("1.Tinh dien tich hinh vuong")
print("2.Tinh dien tich hinh chu nhat")
print("3.Tinh dien tich hinh tam giac")
print("4.Thoat")

a = int(input("Lua chon cua ban: "))


def calSquare():
    print("1.Tinh dien tich hinh vuong")
def calRetAngle():
    print("2.Tinh dien tich hinh chu nhat")
def calTriAngle():
    print("3.Tinh dien tich hinh tam giac")
def exit():
    print("Chon chuc nang muon thuc hien")
    print("1.Tinh dien tich hinh vuong")
    print("2.Tinh dien tich hinh chu nhat")
    print("3.Tinh dien tich hinh tam giac")
    print("4.Thoat")


if a == 1:
    calSquare()
elif a==2:
    calRetAngle()
elif a==3:
    calTriAngle()
else:
    exit()

