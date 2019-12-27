print("Nhap mot so tu ban phim va in ra tong cac so tu 1 den so vua nhap")

a = int(input("Nhap so bat ky: "))

tong = 0
i = 1
while i < a:
    tong = tong + i
    i += 1

print("Tong cac so tu 1 den "+str(a)+" la: "+str(tong))

print("In ra cac so le tu 100 - 50")

i = 100
while i > 50:
    if i%2 == 1:
        print(str(i))
    i -= 1