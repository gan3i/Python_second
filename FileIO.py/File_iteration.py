import sys 

# f = open(sys.argv[1],mode='rt',encoding="utf-8")
f = open("wasteland.txt",mode='rt',encoding="utf-8")

for line in f:
    sys.stdout.write(line)# will not add newlines like print

f.close()

