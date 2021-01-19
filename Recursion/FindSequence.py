## Read input as specified in the question.
## Print output as specified in the question.

def findNum(s,n):
    if int(s+"5")<n:
        print(int(s+"5"))
        findNum(s+"5",n)
    if int(s+"2")<n:
        print(int(s+"2"))
        findNum(s+"2",n)

if __name__=="__main__":
    n=int(input())
    findNum("",n)
        