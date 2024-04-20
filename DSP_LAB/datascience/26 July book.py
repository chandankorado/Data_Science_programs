book = {}
book['tom'] = {'name':'tom','add':'1 red street,NY','ph':'234'}
book['bob'] = {'name':'bob','add':'1 blue street,NY','ph':'123'}

import json

s = json.dumps(book)
with open("C://Users//ALAKHA BEHERA//Desktop//datascience//1basics//book.txt","w") as f:
    f.write(s)
