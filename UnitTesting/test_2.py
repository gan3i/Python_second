
def save_change(y):
    # with (f as open("list.txt")):
    f = open("list.txt", mode="wt", encoding="utf-8")
    f.write(y)

l=1
print ("Please input five numbers")
a=int(input("1.:"))
print (a, "is the first number.")
print()
b=int(input("2.:"))
print (b, "is the second number.")
print()
c=int(input("3.:"))
print (c, "is the third number.")
print()
d=int(input("4.:"))
print (d, "is the fourth number.")
print()
e=int(input("5.:"))
print (e, "is the fifth number.")
print()

x=[a, b, c, d, e]
y=sorted(x,reverse=True)

print (y)
save_change()
while l==1:
    print()
    print ("If you want to delete a number, press D.")
    print()
    print ("If you want to add a number, press A.")
    print()
    print ("If you want to change a number, press C.")
    print ()
    print ("If you want to exit, press Q.")
    print ()
    z=input("Answer: ")

    if z=="A":
        f=int(input("Please input another number: "))
        x.append(f)
        y=sorted(x,reverse=True)
        print (y)

    elif z=="C":
        g=int(input("Input a number you will change: "))
        if g in x:
            x.remove(g)
            print (g, "is removed.")
            f=int(input("Put the number you want to replace: "))
            x.append(f)
            y=sorted(x,reverse=True)
            print (y)

        elif g not in x:
            print ()
            print (g, "is not in the list.")
            y=sorted(x, reverse=True)
            print (y)

        elif z=="D":
            g=int(input("Input a number you will delete: "))
            if g in x:
                x.remove(g)
                print (g, "is removed.")
                y=sorted(x,reverse=True)
                print (y)
            elif g not in x:
                print ()
                print (g, "is not in the list.")
                y=sorted(x, reverse=True)
                print (y)
        elif z=="Q":
                import sys
                print ("Thanks!")
                sys.exit
                break
        else:   
            print ("Sorry. I could not understand. Try again.")



