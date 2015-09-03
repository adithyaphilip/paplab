l = list(map(int, input().split()))
print([sum(l[0:i+1]) for i in range(len(l))])
