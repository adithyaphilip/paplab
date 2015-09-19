ip = input().split('/')
if len(ip) == 3:
    tl =  [i for i in ip if i.isdigit()]
    if len(tl) != 3:
        print ("Invalid")
        quit()
    if len(tl[0]) != 2 or len(tl[1]) != 2 or len(tl[2]) != 4:
        print("Invalid")
        quit()
    (d,m,y) = map(int, tl)
    if y > 9999:
        print("Invalid")
        quit()
    lm = [9,4,6,11] 
    feb = [2]
    rest = [i for i in range(1,13) if i not in lm and i not in feb]
    if m <=12 and m>0 and d>0:
        if m in rest: 
            if d <= 31:
                print('Valid')
                quit() 
        elif m in lm:
          if d <= 30:
                print("Valid")
                quit()
        elif m in feb:
            if d<=29 and y%4==0 or d<=28:
                print("Valid")
                quit()
print("Invalid")
