#Let the Graph G(V,E) with
V = [0,1, 2, 3, 4]
E = [(0,1),(0,2),(0,3),(1,3),(2,3),(3,4)]


print("Vertices:", V)
print("Edges:", E)


#adjacent matrix
n=len(V)
L = [[0]*n for _ in range(n)]

for i in range(len(V)) :
    for j in range(len(V)) :
        if (V[i], V[j]) in E or (V[j], V[i]) in E :
            L[i][j] = 1

for row in L:
    print(row)
    
#adjacency list
G={}
for i in range(len(V)):
    G[V[i]]=[]
    for j in range(len(V)):
        if (V[i], V[j]) in E or (V[j], V[i]) in E :
            G[V[i]].append(V[j])
print(G)
