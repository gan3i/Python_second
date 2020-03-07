#immutable sequence of orbitrary objects

t=("hey",2,4,5)

print("first="+t[0]+ " Second=" + str(t[1]) +" length=" +str(len(t)))

t+(48,34)
t=t*3
for i in t:
    print(str(i))


p=((3,3),4,4)

print(p[0][1])

singletuple=(343,)

emptytuple=()

#tuple unpacking

def return_min_max(item):
    return min(item),max(item)

emptytuple=return_min_max([1,2,3,4])

minx,max=return_min_max([1,2,3,4])

print(emptytuple[0],emptytuple[1])


(a,(b,(c,d)))=(1,(2,(3,4)))

print(a,b,c,d)

a="jelly"
b="bean"

a,b=b,a #swapping 

x=tuple([1,2,3,3,])

print(a +b)

print(5 in x)
print(3 not in x)
