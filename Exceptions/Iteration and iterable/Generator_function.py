#iterables defined by functions. a function acts as a iterable and returns value
#sequences are lazy evaluated
# allows to model sequence with no deinite end.
#can be composed to pipelines
# must contain at least one yield.
# they may also contain the return keyword,
#  and just like any other fucntion there is a implicit return at the end.


def gen123():
    yield 1
    yield 2
    yield 3

g= gen123()
print([next(g),next(g),next(g)])

f = gen123()
for v in gen123():
    print(v)

h = gen123()
j = gen123()

print(h is j)


def gen246():
    print("yield 2")
    yield 
    print("yield 4")
    yield 4
    print("yield 6")
    yield 6
    print("return")

k=gen246()

for v in k:
    print(v)


