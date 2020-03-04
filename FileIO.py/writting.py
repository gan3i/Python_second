# file : path of the file, this is required.
# mode : read, wrirte or append plus binary or text. this is optional parameter.
# encoding : emcoding to use in text mode.
# binary mode reads and writes data inbinary format no matter how the file is stored on disk.
# text mode reads and writes data with the use of encoding and decoding provided.

import sys

print(sys.getdefaultencoding())

f = open("wasteland.txt", mode="wt", encoding="utf-8")
# read = r
# write = w
# append = a
# text = t
# binary = b

# help(f)

print(f.write("what are the roots that clutch, "))#returns number of characters written to the file not the bites.
f.write("what brancher grow\n, ")
f.write("out of this tony rubbir ")
f.close()