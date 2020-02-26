def sqrt(x):
    """Compute square root of a number using the method of heron and Alexandria

    args:
        x: the number of which square root has to be computed
        
    returns: 
        The square root of x
    """
    guess=x
    i=0
    while guess*guess !=x and i<20:
            guess = (guess + x /guess)/2.0
            i +=1
        
    return guess


def main(x):
    try:
        print(sqrt(x))
    except ZeroDivisionError:
            print("cannot calculate the square root of negative number ")
            raise ValueError("Cannot Compute the Square root of "f"Negative number {x}")

if __name__=="__main__":
    main(-1)

    