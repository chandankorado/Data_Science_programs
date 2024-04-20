f1 = open("file1.txt","r")
f2 = open("file2.txt","r")

t1 = f1.read()
t2 = f2.read()

f1.close()
f2.close()

f1 = open("file1.txt","w")
f2 = open("file2.txt","w")

f1.write(t2)
f2.write(t1)

f1.close()
f2.close()