#EAFP It's easier to ask forgiveness than permision.
#LBYL-Look before you leave.

import sys
from math import log 

DIGIT_MAP = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def convert(s):
    try:
        number = ""
        for token in s:
            number += str(DIGIT_MAP[token])
        x=int(number)        
        print("Coversion succeeded!")
    except KeyError as e:#(KeyError,TypeError)
        # print("Conversion failed! Key error" + str(e))
        print(f"Conversion failed! Key error: {e!r}",file=sys.stderr)
        print(e)
        # x= -1
        raise
    except TypeError as e:
        print("Conversion failed! Type error" + str(e))
        # x= -2 
        raise
    except :
        pass
    finally:
        pass
    return x

# Exceptions cannot be ingnored
def string_log(s):
    v=convert(s)
    return log(v)
