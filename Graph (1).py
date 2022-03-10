from collections import defaultdict
import math
s, b, c, d, e = 's', 'b', 'c', 'd', 'e'
graph = {s: {b: 6, c: 1, d: 7, e: 4},
         b: {s: 6},
         c: {s: 1, d: 3, e: 2},
         d: {s: 7, c: 3},
         e: {s: 4, c: 2}
         }

def dijkstra(G, s):
    """
    :param G: graph as a dictionary of dictionaries
    :param s: source vertex
    :return: Dist, dictionary, where Dist[v] is the distance from source to v
    :return: Prev, dictionary, where Prev[v] is previous vertex on the shortest way to v
    """
    Dist = defaultdict(lambda: math.inf)
    Prev = defaultdict(None)
    Dist[s] = 0
    V = list(G.keys())
    Rem = V.copy()
    while len(Rem) > 0:
        u = Rem[0]
        u_value = Dist[u]
        for x in Rem[1:]:
            if Dist[x] < u_value:
                u = x
                u_value = Dist[x]
        Rem.remove(u)
        for v in G[u]:
            if v in Rem:
                Z = min(Dist[v], Dist[u] + G[u][v])
                if Z < Dist[v]:
                    Dist[v] = Z
                    Prev[v] = u
    return Dist, Prev

#D, P = dijkstra(graph, s)
#print(D)
#print(P)

def generate():
    return defaultdict(int)

filename = 'E:\\nct\\in.txt'
file = open(filename, 'r')
lines = file.readlines()
# edges = []
# for line in lines:
#     edges.append(line.split())

edges = [line.split() for line in lines]

#graph2 = defaultdict(lambda: defaultdict(int))
graph2 = defaultdict(generate)

for e in edges:
    vertex = e[0]
    adj_vertex =e[1]
    weight = int(e[2])
    graph2[vertex][adj_vertex] = weight
    graph2[adj_vertex][vertex] = weight    

for v in graph2:
    for u in graph2[v]:
        print(u, ' ', v, ' :', graph2[u][v])


def __dfs__(G, s, result, visited):
    result.append(s)
    visited[s] = True
    for v in G[s].keys():
        if visited[v] == False:
            __dfs__(G,v,result, visited)

def dfs(G,s):
    result = []
    def return_False():
        return False
    visited = defaultdict(return_False)
    __dfs__(G,s,result, visited)
    return result

print(dfs(graph,s))
print(dfs(graph2,s))










