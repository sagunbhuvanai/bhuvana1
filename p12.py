m=5
for i in range(1,m+1):
    for j in range(1,m+1):
        if(i<=j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
