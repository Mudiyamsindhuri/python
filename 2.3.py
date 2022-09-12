b=int(input("enter the lengthof array"))
a=[]
e=[]
for i in range(0,b):
    c=input("enter the string")
    a.append(c)
for i in range(0,b):
    d=len(a[i].split())
    e.append(d)
print("List=",a)
print("max words in a string=",max(e))
