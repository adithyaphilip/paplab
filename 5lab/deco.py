def decoStar(f):
    def inner(m):
        print("*"*5)
        f(m)
        print("*"*5)
    return inner
def decoDollar(f):
    def inner(m):
        print("$"*5)
        f(m)
        print("$"*5)
    return inner

@decoDollar
@decoStar
def print_message(m):
    print(m)
print_message("hello")
