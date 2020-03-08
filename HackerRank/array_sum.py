N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray=[]
for i in range(0,N):
    sumArray.append(numArray1[i] + numArray2[i])

# Write the logic here:



# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")