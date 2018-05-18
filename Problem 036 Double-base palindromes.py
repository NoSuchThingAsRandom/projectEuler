import math
def check_palindrome(test):
    if len(test)%2==0:
        return test[:int(len(test)/2)]==test[int(len(test)/2):][::-1]
    else:
        return test[:int(len(test)/2)]==test[int(len(test)/2)+1:][::-1]

def convert(num):
    size=(int(math.log(num,2)))
    val=""
    for x in range(size+1,0,-1):
        if num>=2**x:
            num-=2**x
            val+="1"
        else:
            val+="0"
    if num==1:
        val+="1"
    else:
        val+="0"
    if val[0]=="0":
        val=val[1:]
    return(val)

denary_nums=[]
for x in range(1,1000000):
    if(check_palindrome(str(x))):
        denary_nums.append(x)
total=0
binary_nums=[]
for x in denary_nums:
    if check_palindrome(str(convert(x))):
        total+=x
        binary_nums.append(x)
print(binary_nums)
print(total)
