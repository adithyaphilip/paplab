l = list(map(eval, input().split()))
print("Sorted:",sorted(l,key=lambda x: int(x[1].split('/')[2])))
for i in range(1,13):
    s = [t for t in l if int(t[1].split('/')[1]) == i]
    if (len(s) > 0): print("Born in month", i, s)

