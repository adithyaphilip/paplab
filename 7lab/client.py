import Area
def menu():
    print("1. Circle", "2. Rectangle", "3. Triangle", sep="\n")
    sw = {1:Area.circle, 2:Area.rect, 3:Area.tri}
    inp = input().split()
    r = sw[int(inp[0])](*map(int, input().split()))
    if (r!=None):
        print(r)
menu()
