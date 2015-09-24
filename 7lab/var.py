class Account:
    accno = 0
    def __init__(self, name, address):
        self.name= name
        self.address = address
        Account.accno+=1
        self.accno = Account.accno
    def disp(self):
        print(self.name, self.address, sep=",")
class FDAccount(Account):
    def __init__(self, name, address, amt, years, r):
        super().__init__(name,address)
        self.amt = amt
        self.years = years
        self.r = r
        self.trans = 0
    def totalAmount(self):
        return self.amt*self.years*self.r
    def deposit(self, amt):
        self.amt+=amt
        self.trans+=1
    def withdraw(self, amt):
        if (self.amt< amt): print("Insufficient funds")
        else:
            self.amt-=amt
            self.trans+=1
a = FDAccount("John","Road street", 100, 1, 1.0)
print(a.accno)
b = FDAccount("Mark", "Khan Residency", 200, 1, 1.5)
c = FDAccount("Ramu", "Baru Mansion", 1000, 5, 2.5)
print(a.accno, b.accno, c.accno)
print(a.totalAmount(), b.totalAmount(), c.totalAmount())
a.deposit(10000)
b.deposit(100000)
b.withdraw(100000)
l = list((a,b,c))
l.sort(key=lambda x: x.trans, reverse=True)
for i in l:
    i.disp()
    print(i.trans, i.totalAmount())
