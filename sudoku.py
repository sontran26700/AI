from collections import defaultdict, deque
import sys
data = open('E:\in.txt','r')
lines=data.readlines()
arr=[]
for i in lines:
	arr.append(i.split())
#print(arr)
nodes=[]
for j in range(len(arr)):
	nodes.append(str(arr[j][0]))
	nodes.append(str(arr[j][1]))
#print(nodes)
#print(dist)
#print(arr)
#print(lines)
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    graph = Graph()
   	#for i in data:
   	#	print(i)

    for i in nodes:
    	#print(i)
        graph.add_node(i)
    	
    for i in range(len(arr)):
    	graph.add_edge(arr[i][0],arr[i][1],int(arr[i][2]))


    

    print(shortest_path(graph, '0', '4')) 