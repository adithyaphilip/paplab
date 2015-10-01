class fib:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.c = self.a+self.b
    def __iter__(self):
        return self
    def __next__(self):
        if(self.a<=self.n):
            t = self.a
            self.a = self.b
            self.b = self.c
            self.c = self.a+self.b
            return t
        else: raise StopIteration

for i in fib(int(input())):
    print(i)
