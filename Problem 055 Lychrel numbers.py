def check_palindrome(num):
    val=num
    length=len(val)
    if length%2==0:
        if val[:int(length/2)]==val[int(length/2):][::-1]:
            return True
    else:
        if val[:int(length/2)]==val[int(length/2)+1:][::-1]:
            return True
    return False
def lychrel(num):
    val=str(num)
    for x in range(0,50):
        if check_palindrome(val):
            return False
        else:
            val=str(int(val[::-1])+int(val))
    return True

count=0
for x in range(0,10000):
    if (lychrel(x)):
        count+=1
        print(x)
print("Total: "+str(count))
