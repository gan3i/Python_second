
def lucas():
    yield 2
    a=2
    b=1
    while True:
        yield b
        a,b = b, a + b


def print_Lucas():
    for i in lucas():
        c=0
        if c == 5: #otherwise loop will run forever.
            print(i)
            c +=1



print_Lucas()
        