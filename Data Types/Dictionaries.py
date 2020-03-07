#heart of python programs
#keys must be unique values can be duplicate
#keys objects must be immutable(str,numbers,tuple)
#vlaue objects can be mutable
#order of the items are random do not relay on them
urls={"google":"http:/google.com",
    "Pluralsight":"http:/Pluralsight.com",
    "sixty-north":"http:/sixty-north.com",
    "Microsoft":"http:/microsoft.com"}

print(urls["google"])
# print(urls[0])

name_and_age = [('bob',32),("Alice",23),("Daniel",25)]

d= dict(name_and_age)

print(d)

C=dict(bob="23",b="45",c="23")

print(C)

updated= d.update(C)

print(d)

# Dictionary yields next key on each iteration

for i in d:
    print(d[i])


for i in d.values():
    print(i)


for i in d.keys():
    print(i)

print("hello")
for i in d.items():#yields each key value pair as tuple
    for j in i:
        print(j)


for i,j in d.items():# tuple unpacking
    print(i)
    print(j)


#membership opertaors work on the keys

if("bob" in d):
    print("bob-true")


if("bob" not in d):
    print("bob-ture")


del d["bob"]

print(d)


m = {"a":[1,2,3],
    "b":[3,4,4]
    }

m["b"] += [9,6,7]

print(m)

m["N"]=[2,3,4]

print(m)

from pprint import pprint as pp

pp(m)
