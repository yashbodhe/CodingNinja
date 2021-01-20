## Read input as specified in the question.
## Print output as specified in the question.
def check(n): 
    count0,count1 = 0,0
    if n==0:count0=1
    while (n): 
        if n & 1:
        	count1 += 1
        else:
            count0 +=1
        n >>= 1
    if count1==count0:
        return True
    return False

n=int(input())
a=list(map(int,input().split()))
res=0
for x in a:
    if check(x):
        res+=x
print(res)