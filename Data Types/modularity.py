def nth_root(radicant, n):
    return radicant ** (1/n)



def ordinal(n):
    s=str(n)
    if s.endswith("11") or s.endswith("12") or s.endswith("13"):
        return "th"
    elif s.endswith("1"):
        return "st"
    elif s.endswith("2"):
        return "nd"
    elif s.endswith("3"):
        return "rd"
    else:
        return "th"



def display_nth_root(radicant,n):
    root= nth_root(radicant,n)
    message= "The " + str(n)+ordinal(n) + " root of "\
        +str(radicant) + " is " + str(root)
    print(message)
    
    
print(__name__)   
# if __name__== "__main__":
#     display_nth_root(27,14)


# print(__name__)








