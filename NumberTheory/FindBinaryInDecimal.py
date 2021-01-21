## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
res=0
q=["1"]
while q:
    x=q.pop(0)
    res+=1
    if int(x+"1")<=n:
        q.append(x+"1")
    if int(x+"0")<=n:
        q.append(x+"0")
print(res)