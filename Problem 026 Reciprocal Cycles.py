def contains(prev,targ):
    for x in prev:
        if x==targ:
            return True
    return False

def calc(x):
    count=0
    prev=[]
    val=1%x
    while contains(prev,val)==False:
        prev.append(val)
        val=((10*val)%x)
        if val==0:
            return -1
        count+=1
    return count

high=0
target=0
for x in range(1,1000):
    score=calc(x)
    if score>target:
        target=score
        high=x
print(str(high)+" was the highest with a repetition of "+str(target))
