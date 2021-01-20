## Read input as specified in the question.
## Print output as specified in the question.
def check(n,zero,one): 
    count0,count1 = 0,0
    if n==0:count0=1
    while (n): 
        if n & 1:
        	count1 += 1
        else:
            count0 +=1
        n >>= 1
    if one==count1 and zero==count0:
        return True
    return False

n=int(input())
a=list(map(int,input().split()))
zero=int(input())
one=int(input())
res=0
for x in a:
    if check(x,zero,one):
        res+=x
print(res)