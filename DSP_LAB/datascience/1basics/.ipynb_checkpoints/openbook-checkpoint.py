f = open("C://Users//ALAKHA BEHERA//Desktop//datascience//1basics//book.txt","r")
s = f.read()
print(s)

import json
st = json.loads(s)
print(st)
print(type(st))

for person in st:
    print(st[person])
