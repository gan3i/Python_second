import numpy as np

def main():
    from sys import stdin, stdout

    n,q=(5,3)#map(int,stdin.readline().split())
    a= np.arange([1,2,3,4,5])
    s= slice(2,4)
    sub_array = a(s)
    print(sub_array)
    # for x in [1,2,3,4,5]:
    #     A.append(int(x)+A[-1])
    #     print(A)
    # res=""
    # for Inp in ["2 5"]:
    #     l,r=map(int,Inp.split())
    #     n=r-l+1
    #     S=A[r]-A[l-1]
    #     res+=str(S//n)+"\n"
    # stdout.write(res)
 
if __name__ == "__main__":
    main()

print(3//3)

