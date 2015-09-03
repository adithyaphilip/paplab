theD = {}
def addWord():
    w,m = input().split(":")
    theD[w]=m
def rem():
    w = input()
    print("Deleted:", theD.pop(w))
def findMeaning():
    w = input()
    print("Meaning:", theD[w]);
def findWord():
    m = input()
    print("Words:", ", ".join([i for i in theD if theD[i]==m]))
def sort():
    print("Sorted: ", [key for key in sorted(theD)])
def printDict():
    print(theD)
def menu():
    print("1. Add", "2. Remove", "3. Find meaning", "4. Find word", "5. Print sorted words", "6. Print dictionary", sep='\n') 
menu()
s = int(input())
while s<7:
    opt = {1:addWord, 2:rem, 3:findMeaning, 4:findWord, 5:sort, 6:printDict}
    opt[s]()
    menu()
    s = int(input())



