import sys
def circle(*r):
    if(__name__ == '__main__' and len(sys.argv)!=3): print("Error: Circle requires exactly 1 argument"); return
    elif (__name__ == '__main__'): 
        r = [int(sys.argv[2])]
    r = r[0]
    return 3.14*r**2

def rect(*t):
    if(__name__ == '__main__' and len(sys.argv)!=4): print("Error: Incorrect number of arguments (2 required)"); return 
    elif (__name__ == '__main__'): 
        t = int(sys.argv[2]),int(sys.argv[3])

    a,b = t
    return a*b

def tri(*t):
    if(__name__ == '__main__' and len(sys.argv)!=5): print("Error: Incorrect number of arguments (3 required)"); return
    elif (__name__ == '__main__'): 
        t = list(map(int, sys.argv[2:]))
    a,b,c = t
    s = a+b+c
    return (s*(s-a)*(s-b)*(s-c)/2)**0.5

if (__name__=='__main__'):
    sw = {"circle":circle, "rectangle":rect, "tri":tri}
    try: 
        r = sw[sys.argv[1]]()
        if r != None:
            print(r)
    except (KeyError, IndexError) as e:
        print("Invalid Input")
