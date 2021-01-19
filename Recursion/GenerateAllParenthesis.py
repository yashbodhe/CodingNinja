## Read input as specified in the question.
## Print output as specified in the question.

def findNum(s,n1,n2,n):
    if n1==n and n2==n:
        print(s)
    if n1<n:
        findNum(s+"(",n1+1,n2,n)
    if n2<n1:
        findNum(s+")",n1,n2+1,n)

if __name__=="__main__":
    n=int(input())
    findNum("",0,0,n)
        