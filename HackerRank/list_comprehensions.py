import time

x = int (input())
y = int (input())
z = int (input())
n = int (input())
ar = []
p = 0

time_now = time

for i in range ( x + 1 ) :
    for j in range( y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [ i , j ]
            p+=1
print(ar)

# with list comprehension



print([ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1 ) if ( ( i + j + k ) != n )])


# using "%" to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.2f'%a) 
  
# using format() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using format()) is : ",end="") 
print ("{0:.2f}".format(a)) 
  
# using round() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using round()) is : ",end="") 
print (round(a,2))

