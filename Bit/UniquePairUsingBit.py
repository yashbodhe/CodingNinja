## Read input as specified in the question.
## Print output as specified in the question.
if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    summ=0
    for x in a:
        summ=summ^x
    summ=(summ&-summ)
    x1,x2=0,0
    for x in a:
        if summ&x>0:
            x1=x1^x
        else:
            x2=x2^x
    if x1<x2:
        print(x1,x2)
    else:
        print(x2,x1)