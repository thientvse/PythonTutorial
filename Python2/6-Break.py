print("In ra nhung so chia het cho 7 trong khoang 300-500")

i = 300;
while i < 500:
    if i%7 == 0:
        print(str(i))
    i += 1

print("Dung lenh break")
i = 300;
while i < 500:
    if i == 400:
        break
    if i%7 == 0:
        print(str(i))
    i += 1

print("Dung lenh continue")
i = 300;
while i < 500:
    if i == 350:
        continue
    if i%7 == 0:
        print(str(i))
    i += 1