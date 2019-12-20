print("-----------Tinh thue cho nhan vien-----------")
a = int(input("Nhap so gio lam viec: "))
b = int(input("Luong theo gio: "))

if a > 40 :
   tienThemGio = (a - 40)*b*1.5
   luongTruocThue = 40 * b + tienThemGio

   print("Muc luong truoc thue: " + str(luongTruocThue))
   print("\nMuc luong sau thue: " + str(luongTruocThue * 0.9))

else:
   print("Muc luong truoc thue: "+str(a*b))
   print("\nMuc luong sau thue: "+str((a*b)* 0.9))
