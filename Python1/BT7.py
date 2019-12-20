print("Tinh tien dien")
a = int(input("Nhap so luong dien tieu thu: "))

if a <= 100 :
    tiendien = a * 450
elif a > 100 & a < 201 :
    tiendien = 100 * 450 + (a-100)*600
elif a > 200 & a < 301 :
    tiendien = 100 * 450 + 100*600 + (a-200)*750
elif a > 300 & a < 501 :
    tiendien = 100 * 450 + 100 * 600 + 100 * 750 + (a - 300) * 900
elif a > 500 & a < 1001 :
    tiendien = 100 * 450 + 100 * 600 + 100 * 750 + 200 * 900 + (a-500)*1000
elif a > 1000 :
    tiendien = 100 * 450 + 100 * 600 + 100 * 750 + 200 * 900 + 500 * 1000 + (a-1000)*1200

print("Tien dien truoc thue: " + str(tiendien))
print("\nTien dien sau thue: " + str(tiendien + tiendien*0.1))