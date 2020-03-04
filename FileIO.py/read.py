

r=open("wasteland.txt",mode="rt",encoding="utf-8")

print(r.read())# to read all the content
print(r.read())# subsiquent reads return empty string

print(r.seek(0))# seeting it back to begining of the string, returns index it was set back to
print(r.read(32))


print(r.seek(0))
print(r.readline())
print(r.readlines())
print(r.readable())

print(r.seek(0))

r.close()