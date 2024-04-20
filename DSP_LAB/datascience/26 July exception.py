x = input("Enter a number : ")
y = input("Enter another number : ")
try:
    z = int(x) / int(y)
except Exception as e:
    print("Exception is occured : ",e)
    z = None
print("Division is : ",z)
