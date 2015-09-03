n = int(input())
l = [[1]]
for i in range(1, n):
    l.append([1])
    l[i]+=[l[i-1][x-1] + l[i-1][x] for x in range(1,i)]
    l[i].append(1) 
for i in range(n):
    print(" "*(n-1-i) + " ".join(map(str, l[i])))
