from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def bfs(adj,verticies):
    res=[0 for i in range(verticies + 1)]
    for i in range(1,verticies+1):
        q=[i]
        visit=[0 for i in range(verticies + 1)]
        visit[i]=1
        while q:
            u=q.pop(0)
            for v in adj[u]:
                if not visit[v]:
                    visit[v]=1
                    q.append(v)
        res[i]=visit.count(1)
    return res[1:]

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
    
res=bfs(adj,verticies)
for x in res:
    print(x)
