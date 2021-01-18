
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def bfs(adj,verticies):
    visit=[0 for i in range(verticies + 1)]
    for i in range(1,verticies+1):
        if not visit[i]:
            q=[i]
            visit[i]=1
            while q:
                u=q.pop(0)
                for v in adj[u]:
                    if not visit[v]:
                        visit[v]=3-visit[u]
                        q.append(v)
                    elif visit[v]==visit[u]:
                        return "NO"
    return "YES"

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
    
print(bfs(adj,verticies))



