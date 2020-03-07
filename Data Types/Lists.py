L=[1,2,3,3,4,6]

print(L[-1])#negative indexing is one based.
print(L[-0],L[0])

# slicing is extended for of indexing.
# List[start:stop] both start and stop indecis are optional.

print(L[1:4])

print(L[1:-1])

print(L[2:])

print(L[:])

print(L[:2])

S=L
print(S is L)

R=L[:]#shallow copy

print(R is L)
print(R==L)
# all these methods word fine on any iterable
P=L.copy()#shallow copy

print(P is L)

Q=list(L)#shallow copy

print(Q is L)

A=[[1,2],[3,4]]

B=A.copy()

print(A is B)
print(A==B) 
print(A[0] is B[0])

A[0]=[9,9,9]
print(A[0] , B[0])

A[1].append(444)

print(B[1])

#copy module has more to offer for true deep copying.

print(L*3)

T=L*3
T[0]=999

print(T)
print([0]*3)

Y=[[9,8]]*3
print(Y)

# Y[0]=44
Y[0].append(44)

print(Y)

Y[0]=[44,33,44]


print(Y)
print(Y.index([9,8,44]))

K="the quick brown fox jumps over the lazy dog".split()

print(K.index("dog"))
print(K.count("the"))
print("the" in K)
print("the" not in K)
# print(K.index("dogt"))

del Y[0]# position
del K[K.index("over")]#index by value

print(Y)

K.remove("the")#by value
K.remove(K[0])#by index
K.remove(K[K.index("fox")])

print(K)

print(K.insert(2,"quick"))
print(" ".join(K))
K.extend(["hey"])
print(K)


K.reverse()
print(K)

K.sort()

print(K)

K.sort(reverse=True)

print(K)

K.sort(key=len)

print(K)

N=[1,4,2,3,0,1]

M=sorted(N)

print(N)
print(M)

G=reversed(N)

print(G)#reverse iterable object.
print(list(G))