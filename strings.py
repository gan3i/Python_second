print(len("sdsdsdsdsdsd"))


print("Hey" + " Pal")

s ="damn this"

print(s)
print(s.join("ABC"))  

print(s.join(["a","b"]))

print("".join(["hey","pal","again"]))

print(";".join(["#256545","#254544","#454545"]))

print("unforgetable".partition("get"))


A,B,C="unforgetable".partition("get")

print(A+" "+B+" "+C)

C,Seperater,D = "London:Edinburgh".partition(":")
C,_,D = "London:Edinburgh".partition(":")

print("{0} north, {1} east".format(59.5,65))
print("{} north, {} east".format(59.5,65))
print("{0} north, {1} east,{0} west".format(59.5,65))
print("{lat} north, {long} east,{west} west".format(long=59.5,lat=65,west=85))
print("{tuplee[0]} north, {tuplee[1]} east,{tuplee[2]} west".format(tuplee=(1,2,3)))
import math
print("math constants pi={m.pi} and e={m.e} ".format(m=math))


def mult(a,b):
    return a*b
f-strings
print(f"multiplication of 2 and 3 is equal to {2*3}")
print(f"multiplication of 2 and 3 is equal to {mult(2,3)}")


import datetime
print(f"curent date time is {datetime.datetime.now().isoformat()}")
print("math constants pi={m.pi:.3f} and e={m.e:.3f} ".format(m=math)) #specifying format

help(str)






