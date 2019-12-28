print("Tinh thue thu nhap")
salary = int(input("Nhap luong cua nhan vien: "))
bonus = int(input("Nhap phu cap cua nhan vien: "))

salaryTruocThue = salary + bonus
salaryCurrent = salaryTruocThue
print("Luong truoc thue: "+str(salaryTruocThue))

salaryChiuThue = salaryTruocThue - 9000

print("Luong chiu thue: "+str(salaryChiuThue))

if 0< salaryChiuThue <= 5000:
    salaryCurrent = salaryTruocThue - (salaryChiuThue*5)/100
    print("Muc thue: 5%")
elif 5000 < salaryChiuThue < 10000:
    salaryCurrent = salaryTruocThue - salaryChiuThue * 0.1
    print("Muc thue: 10%")
elif 10000 < salaryChiuThue < 15000:
    salaryCurrent = salaryTruocThue - salaryChiuThue * 0.15
    print("Muc thue: 15%")
elif 15000 < salaryChiuThue < 20000:
    salaryCurrent = salaryTruocThue - salaryChiuThue * 0.2
    print("Muc thue: 20%")
elif salaryChiuThue > 20000 :
    salaryCurrent = salaryTruocThue - salaryChiuThue * 0.25
    print("Muc thue: 25%")
else:
    print("Khong phai nop thue")

print("Thu nhap thuc te: "+str(salaryCurrent))


