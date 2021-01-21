## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
c=0
while n:
    c+=1
    n=n&(n-1)
print(c)