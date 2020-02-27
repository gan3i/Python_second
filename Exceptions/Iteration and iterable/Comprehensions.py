

words="why sometimes I have believed as many as six imposible things before breakfast".split()

print(words)

# list comprehensions
#[expresion(item) for item in iterable]
word_lentgh = [len(word) for word in words]

print(word_lentgh)

from math import factorial
f =[len(str(factorial(x))) for x in range(20)]

print(f)

# Set comprehension
#{expresion(item) for item in iterable}
word_lentgh_set = {len(word) for word in words}

print(word_lentgh_set)

f_set= {len(str(factorial(x))) for x in range(20)}

print(f_set)# notice duplicates are removed

# dictionary comprehension
# {Key_expresion(item):Value_expresion(item) for item in iterable}

Country_to_Capital = {"UK":"London","Sweden":"stockholm"}

Capital_to_Country = {capital:country for country,capital in Country_to_Capital.items()}

print(Capital_to_Country)

#fuckin no limit to the complexity of the use of comprehensions

import os
import glob

file_sizes = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob("*.py")}

print(file_sizes)

