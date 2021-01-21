## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
res=1
for i in range(2,n+1):
    res*=i
print(res)