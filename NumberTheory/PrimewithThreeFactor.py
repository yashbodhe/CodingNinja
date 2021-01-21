## Read input as specified in the question.
## Print output as specified in the question.

n=int(input())
a=list(map(int,input().split()))
for x in a:
    if int(x**(1/2))==(x**(1/2)) and x>1:
        print("YES")
    else:
        print("NO")