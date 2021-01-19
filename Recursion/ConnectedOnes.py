## Read input as specified in the question.
## Print output as specified in the question.
dp = [0 for i in range(200)] 

def isSafe(mat,i,j,n,m):
    if 0<=i<n and 0<=j<m and mat[i][j]==1:
        return True
    return False

def solve(mat,i,j,n,m):
    dir = [[-1, 0],[1, 0],[1, 1],[1, -1],[-1, -1],[-1, 1],[0, 1],[0, -1]]
    res=0
    for k in range(8):
        if isSafe(mat,i+dir[k][0],j+dir[k][1],n,m):
            mat[i+dir[k][0]][j+dir[k][1]]=2
            res+=solve(mat,i+dir[k][0],j+dir[k][1],n,m)
    return res+1
if __name__=="__main__":
    a=list(map(int,input().split()))
    n,m=a[0],a[1]
    mat=[]
    for _ in range(n):
        mat.append(list(map(int,input().split())))
    res=0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                mat[i][j]=2
                res=max(res,solve(mat,i,j,n,m))
    print(res)
        