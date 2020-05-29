for i in range(1, 5):
    if i == 1:
        print(1)
    else:    
        for j in range(1,i+1):
            print(i*j, end=' ')
        print()
    