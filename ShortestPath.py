from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def bfs(adj,src,des,n):
    if src==des:return 0
    visit=[False for i in range(n)]
    q=[(src,1)]
    visit[src]=True
    while q:
        u,dis=q.pop(0)
        for v in adj[u]:
            if v==des:return dis
            if not visit[v]:
                q.append((v,dis+1))
                visit[v]=True
    return -1

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
        adj[v-1].append(u-1)
    src_des = stdin.readline().strip().split(" ")
    src = int(src_des[0].strip())
    des = int(src_des[1].strip())
    print(bfs(adj,src-1,des-1,verticies))
    