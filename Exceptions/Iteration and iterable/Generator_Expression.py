# (expresion(item) for item in iterable)
from pprint import pprint

million_squares_Generator = (x*x for x in range(100000))
million_squares_list = list((x*x for x in range(100000)))

# million_squares1 = [x*x for x in range(1000000)]


print(million_squares_Generator)
# print(million_squares_list)
 
# print(million_squares1)

million_squares_list1 = list(million_squares_Generator)# this way we exhast the generator and i will not yield any value further

# s = sum(million_squares_Generator)
s = sum(x*x for x in range(100000))

print(s)

# we can add filters at the end of generator expresions

Conditional_sum = sum(x*x for x in range(100000) if x%2==0)

print(Conditional_sum)





