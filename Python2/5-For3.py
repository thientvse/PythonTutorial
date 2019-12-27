print("1. Tinh tong S = 1+2+...+N n nhap tu ban phim")
a = int(input("Nhap so bat ky tu ban phim: "))

S = 0
for i in range (1,a) :
    S = S + i

print("Tong: "+str(S))

print("2. Tinh giai thua cua "+str(a))

giaithua = 1
for i in range (1, a+1):
    giaithua = giaithua*i

print("Ket qua: "+str(giaithua))

print("3. Tong "+str(a)+" so nguyen tu ban phim")

tong = 0
for i in range (1, a+1):
    x = int(input())
    tong = tong + x

print("Ket qua: "+str(tong))

