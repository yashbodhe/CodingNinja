## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
k=int(input())
even,odd=n//2,n//2
if n%2!=0:odd+=1
if k<=odd:
    print(k*2-1)
else:
    k-=odd
    print(k*2)