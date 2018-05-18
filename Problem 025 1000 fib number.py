a=1
b=1
c=1
count=2
while len(str(c))<1000:
    c=a+b
    a=b
    b=c
    #print(c)
    count+=1
print("The first number is: "+str(c)+"\nWith an index of: "+str(count))
