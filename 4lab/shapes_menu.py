from Shapes import *
def circl():
    r = int(input())
    print(circle.area(r), circle.circ(r))
def squar():
    a = int(input())
    print(square.area(a), square.peri(a))
def triangl():
    a,b,c = map(int, input().split())
    print(triangle.area(a,b,c), triangle.perimeter(a,b,c))
def menu():
    choice = {1: circl, 2: squar, 3: triangl, 4:quit}
    print("1. Circle", "2. Square", "3. Triangle", "4. Quit")
    choice[int(input())]()
while True:
    menu()


    
