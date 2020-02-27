# al  three type of comprehensions support an optional filtering class

import math
import pprint
def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


prime_series = [x for x in range(0,20) if is_prime(x)]

print(prime_series)

prime_square_series = {x*x:(1,x,x*x) for x in range(20) if is_prime(x)}

pprint.pprint(prime_square_series)

#comprehensions should only be used without side effects if we need side 
# effect like printing to console use for loop instead


    