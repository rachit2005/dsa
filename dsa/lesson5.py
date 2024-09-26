# Lesson 5 - Graph Algorithms (BFS, DFS & Shortest Paths)
# https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-5-graph-algorithms-bfs-dfs-shortest-paths

n = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]

class Graph:
    def __init__(self , n_vertices , edges_list):
        # creating an individual list for 0 ,1,2,3,.. n_vertices-1
        self.data = [[] for _ in range(n_vertices)]

        for v1 , v2 in edges_list:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

    def __repr__(self):
        result = ''
        for index , node in enumerate(self.data):
            # index is index of the node 
            result += str(index)+ " is connected to the following "+str(node) + '\n'

        return result

    def __str__(self):
        return self.__repr__()

graph1 = Graph(n , edges)
# print(graph1)

class graphMatrix:
    def __init__(self , vertices , edges_list):
        # creating an 0 matrix 
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

        for v1 , v2 in edges_list:
            self.matrix[v1][v2] = 1 #assigning 1 value to v1 row and v2 column
            self.matrix[v2][v1] = 1
        
def breadth_first_search(graph , starting_node):
    visited = [False]*len(graph.data) #marking false on all vertices
    queue = []
    queue.append(starting_node) #adding the starting node in the queue
    distance = [0]
    visited[starting_node] = True
    parent = [None]
    i = 0

    while i < len(queue):
        current_node = queue[i] #current node is the starting node as we have added it in the queue
        for adjacent_node in graph.data[current_node]:
            if not visited[adjacent_node]:
                queue.append(adjacent_node) #adding the adjacent nodes in the queue for visiting next
                visited[adjacent_node] = True
                distance.append(distance[current_node] + 1)
                parent.append(current_node)

        i +=1 

    return queue , distance , parent


def dfs(graph , root_node):
    # queue = [] #queue is first in first out
    visited = [False]*len(graph.data)
    stack = [] #stack is last in first out
    stack.append(root_node) #adding element in the last
    result = []

    while len(stack) > 0:
        current_node = stack.pop() #removing and storing the last element of the stack
        if not visited[current_node]:
            result.append(current_node)
            visited[current_node] = True

            for _ in graph.data[current_node]:
                stack.append(_) #adding child node in the stack

    return result

print(dfs(graph1 , 0))

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]

class Graph2:
    def __init__(self, num_nodes, edges, directed=False):
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        
        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3
            
        for v1 , v2, w in edges:
            self.data[v1].append(v2)
            if self.weighted:
                self.weight[v1].append(w)
            
            if not directed: #if not false then it is a two way street
                self.data[v2].append(v1)
                if self.weighted:
                    self.data[v2].append(w)
                
    def __repr__(self):
        result = ""
        for i in range(len(self.data)):
            pairs = list(zip(self.data[i], self.weight[i]))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __str__(self):
        return repr(self)

# SHORTEST DISTANCE 

def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
        
def shortest_path(graph, source, dest):
    """Find the length of the shortest path between source and destination"""
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []
    idx = 0
    
    queue.append(source)
    distance[source] = 0
    visited[source] = True
    
    while idx < len(queue) and not visited[dest]:
        current = queue[idx]
        update_distances(graph, current, distance, parent)
        
        next_node = pick_next_node(distance, visited)
        if next_node is not None:
            visited[next_node] = True
            queue.append(next_node)
        idx += 1
        
    return distance[dest], distance, parent