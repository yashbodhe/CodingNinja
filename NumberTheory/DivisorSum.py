## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
res=0
for i in range(1,n):
    if n%i==0:res+=i
print(res)