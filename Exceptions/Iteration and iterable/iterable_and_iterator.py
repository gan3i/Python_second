# iterable is the equivalent of enumarable.iterable can be can be passed to iter() to get an iterator.
# iterator is the equivalent of enumarator. iterator can be passed to next() to get the next value.


iterable=["spring","summer","autumn","Winter"]

print(iterable)

iterator = iter(iterable)

print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#if print again python will through exception "stopiteration"