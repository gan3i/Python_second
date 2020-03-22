

import time

def fucntion(n):
    i = s = 1
    while s < n:
        i= i + 1
        s = s + i
        print("*")





if "__main__" == __name__:
    start_time = time.time()
    fucntion(20)
    print (time.time() - start_time )
