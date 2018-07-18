m=5

for i in range(1,m+1):
    k=65
    for j in range(1,m+1):
        if(i>=j):
            print(chr(k),end=' ')
            k+=1
    print()
