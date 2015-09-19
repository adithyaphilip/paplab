(a,b) = map(int, input("Enter 2 nums\n").split())
prod = a*b
while a != b:
    if a>b:
        a = a-b
    else:
        b = b-a
print("GCD:", a)
print("LCM:", prod//a)
