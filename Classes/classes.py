
# def return_str():
#     return "str"

# print(type(return_str ))

from airtravel import Flights, Aircraft

print(Flights)

objf=Flights("SN99999")

print(objf)
print(type(objf))

print(objf.number())
print(Flights.number(objf))
print(objf._number)#not recomended for production code

#we are all consenting adults here, so everything is public in python.




