from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def dfsUtil(adj,verticies,x,parent):
    if not visit[x]:
        visit[x]=True
        for i in adj[x]:
            if not visit[i]:
                if not dfsUtil(adj,verticies,i,x):
                    return False
            elif parent!=i:
                return False
    return True
def dfs(adj,verticies):
    global visit
    visit=[0 for i in range(verticies + 1)]
    if not dfsUtil(adj,verticies,1,0):
        return False
    for i in range(1,verticies+1):
        if not visit[i]:
            return False
    return True
                
visit=[False]*99999

#main
verticies_edges = stdin.readline().strip().split(" ")

verticies = int(verticies_edges[0].strip())
edges = int(verticies_edges[1].strip())

adj = [[] for i in range(verticies + 1)]

for i in range(edges) :

    u_v = stdin.readline().strip().split(" ")
    u = int(u_v[0].strip())
    v = int(u_v[1].strip())
    adj[u].append(v)
    adj[v].append(u)
    
if dfs(adj,verticies):
    print("YES")
else:
    print("NO")



