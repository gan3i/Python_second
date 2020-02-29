from itertools import count, islice

d = [1,2,3,4,4,4,3,3,2,2,5]

c = islice(d,2) 

print(c)

print(any([True,False,True,False]))

print(all([False,False,False,False]))

#for Synchronized iteration through two or more iterables,

a = ["hey", "grus", "bitta"]
b = ["Pal!","gott","shoun"]

def print_zip():
    for item in zip(a,b):
        print(item)


print_zip()

# itertol is worth looking at.