#unordered collection of unique elements and are mutable. however each element in set must be immutable.

p={110,2222,3737373737,3,4,5,56,9,2}

print(p)

q=set()# to contruct empty set, it can also create a set from any iterable series and duplicates are discarded.
# sets are iterable. 
r=set([2,343,343,22,4,43])


#member ship test.

print(110 in p)
print(110 not in p)
p.remove(3)# key error if the element is not present
p.discard(3)# not error if the element is not present
t=p.copy() # shallow copy  

print(p.intersection(r))
print(p.intersection(r)==r.intersection(p))
print(p.union(r))
print(p.union(r)==r.union(p))
print(p.difference(r))# are in the first set but not in second set.
print(p.difference(r)==r.difference(p))
print(p.symmetric_difference(r))# ether in first or in second but not in both 
print(p.symmetric_difference(r)==r.symmetric_difference(p))
print(p.issubset(r))# is p subset of r
print(p.issuperset(r))#is p superset of r
print(p.isdisjoint(r))#are p and r not related to each other?


# Protocols
# container- in and not in must be supported.
# Size - len() should be supported .
# iterable - yield element one by one.  
# sequence - intems from searchable using index, count should work, reversed should work and all the above protocols.

