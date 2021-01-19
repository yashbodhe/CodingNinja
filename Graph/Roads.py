from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def dfsUtil(adj,n,x,des,fuel,cost):
    if x==des and cost<=fuel:return True
    elif x==des or cost>fuel: return False
    if not visit[x]:
        visit[x]=True
        for i in range(n):
            if (not visit[i]) and adj[x][i]:
                if dfsUtil(adj,n,i,des,fuel,cost+adj[x][i]):
                    return True
    return False
def dfs(adj,verticies,src,des,fuel):
    global visit
    visit=[0 for i in range(verticies)]
    return dfsUtil(adj,verticies,src,des,fuel,0)
                
visit=[False]*200005

#main
verticies_edges = stdin.readline().strip().split(" ")

verticies = int(verticies_edges[0].strip())
edges = int(verticies_edges[1].strip())
fuel = int(verticies_edges[2].strip())

adj = [[0 for j in range(verticies)] for i in range(verticies)]

for i in range(edges) :
    u_v = stdin.readline().strip().split(" ")
    u = int(u_v[0].strip())
    v = int(u_v[1].strip())
    adj[u-1][v-1]=int(u_v[2].strip())
    adj[v-1][u-1]=int(u_v[2].strip())
src_des = stdin.readline().strip().split(" ")
src = int(src_des[0].strip())
des = int(src_des[1].strip())

if dfs(adj,verticies,src-1,des-1,fuel):
    print("Yes")
else:
    print("No")



