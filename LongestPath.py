from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def dfsUtil(adj,u):
    if dp[u]!=-1:return dp[u]
    sol=0
    for v in adj[u]:
        sol=max(sol,dfsUtil(adj,v))
    dp[u]=sol+1
    return dp[u]

def dfs(adj,src,n):
    global dp
    for i in range(n):
        dp[i]=-1
    dfsUtil(adj,src)
    return dp[src]-1

dp=[-1]*200005
if __name__=="__main__":
    verticies_edges = stdin.readline().strip().split(" ")
    verticies = int(verticies_edges[0].strip())
    edges = int(verticies_edges[1].strip())

    adj = [[] for i in range(verticies)]

    for i in range(edges) :
        u_v = stdin.readline().strip().split(" ")
        u = int(u_v[0].strip())
        v = int(u_v[1].strip())
        adj[u-1].append(v-1)
        
    src_des = stdin.readline().strip().split(" ")
    src = int(src_des[0].strip())
    print(dfs(adj,src-1,verticies))
    