'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main():
    from sys import stdin,stdout

    n,l = map(int,stdin.readline().split())
    array = [0]
    for x in stdin.readline().split():
        array.append(int(x)+array[-1])
    

    res = ""
    for k in stdin.readlines():
        k,j =map(int,k.split())

        num_elements = j-k+1
        array_sum = array[j]-array[k-1]
        
        res =str(array_sum//num_elements) + "\n"
        stdout.write(res)

if "__main__" == __name__:
    main()

        
