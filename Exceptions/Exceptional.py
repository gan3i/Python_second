DIGIT_MAP = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def Convert(s):
    try:
        number = ""
        for token in s:
            number += str(DIGIT_MAP[token])
        x=int(number)        
        print("Coversion succeeded!")
    except KeyError:#(KeyError,TypeError)
        print("Conversion failed! Key error")
        x= -1
    except TypeError:
        print("Conversion failed! Type error")
        x= -2 
    return x
