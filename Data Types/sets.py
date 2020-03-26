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
print("p.difference(r)==r.difference(p)")
print(p.difference(r)==r.difference(p))
print(p.symmetric_difference(r))# ether in first or in second but not in both 
print(p.symmetric_difference(r)==r.symmetric_difference(p))
print(p.issubset(r))# is p subset of r
print(p.issuperset(r))#is p superset of r
print(p.isdisjoint(r))#are p and r not related to each other?


p.add(999)
p.add(999)
p.add((999,888))
#p.add([999,888])# will throw unhashable type: 'list'


#p.update(999) will throw an error if the object is not iterable.
p.update([777,999])
p.update([111,222],{333,555})
print(p)

p.remove(999)
p.discard(777)
# Both the discard() and remove() functions take a single value as an argument and removes that value from the set.
#  If that value is not present, discard() does nothing, but remove() will raise a KeyError exception



# Protocols
# container- in and not in must be supported.
# Size - len() should be supported .
# iterable - yield element one by one.  
# sequence - intems from searchable using index, count should work, reversed should work and all the above protocols.

