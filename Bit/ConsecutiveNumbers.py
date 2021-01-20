## Read input as specified in the question.
## Print output as specified in the question.
def find(k):
    if k==1:return 1
    if k&(k+1)==0:
        return k//2+1
    return -1
k=int(input())
print(find(k))
