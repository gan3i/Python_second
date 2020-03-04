


a=open("wasteland.txt",mode="at",encoding="utf-8")

a.writelines(["Son of man, \n","you cannot say, or guess,","for you know only \n",
                "A heap of broken images"," where the sun beats"])

a.close()

r=open("wasteland.txt",mode="rt",encoding="utf-8")

print(r.read())# to read all the content

r.close()
