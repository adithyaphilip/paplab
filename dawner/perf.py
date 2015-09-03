import math
s,e = map(int, input().split())
def sumD(n):
    res = 0
    while n > 0:
        res+=n%10
        n//=10
    #print (res)
    return res
print([i for i in range(s+1,e) if sumD(i) < 10 and math.sqrt(i) % 1 == 0])
