## Read input as specified in the question.
## Print output as specified in the question.

def findNumU(s,n1,n2,n,res):
    if n1==n and n2==n:
        res.append(s)
    if n1<n:
        findNumU(s+"(",n1+1,n2,n,res)
    if n2<n1:
        findNumU(s+")",n1,n2+1,n,res)
def findNum(n):
    res=[]
    findNumU("",0,0,n,res)
    return res
if __name__=="__main__":
    n=int(input())
    res=findNum(n)
    for x in res:
        print(x)
        