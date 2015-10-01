def right(n):
    l = [(i,j,k) for i in range(1,n+1) for j in range(1,i+1) for k in range(1,j+1)]
    for i in l:
        if i[1]**2+i[2]**2==i[0]**2:
            yield i
for i in right(int(input())):
    print (i)
