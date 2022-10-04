import numpy as np 
import random 
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


# matrix = []

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

# create random edge
def create_random_edge(column_num , edge_num):
    edges = []
    node = np.arange(0,column_num,1)
    for i in node :
        for j in range(i):
            edge= []
            edge.append(i)
            edge.append(j)
            edges.append(edge)
     
    random_edge = random.sample(edges,edge_num)
    return random_edge
      

def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]== 1:
                           adjList[i].append(j)
    return adjList

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1==v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        print('the adjacency matrix :')
        for row in self.adjMatrix:
            print(row)
        matrix = self.adjMatrix
        print()
        return matrix
        
            # for val in row:
            #     print('{:4}'.format(val)),
            # print

# using array , look for components 
class Graph_struct:
   def __init__(self, V):
      self.V = V
      self.adj = [[] for i in range(V)]

   def DFS_Utililty(self, temp, v, visited):

      visited[v] = True

      temp.append(v)

      for i in self.adj[v]:
         if visited[i] == False:
            temp = self.DFS_Utililty(temp, i, visited)
      return temp

   def add_edge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def connected_components(self):
      visited = []
      conn_compnent = []
      for i in range(self.V):
         visited.append(False)
      for v in range(self.V):
         if visited[v] == False:
            temp = []
            conn_compnent.append(self.DFS_Utililty(temp, v, visited))
      return conn_compnent

# to output graph of connected nodes
def visualize(graph):
    G = nx.Graph()
    G.add_edges_from(graph)
    nx.draw_networkx(G)
    plt.show()
     
def main():
    
    node_number = 10
    edge_number = 10
    edges = create_random_edge(node_number,edge_number)
    Matrix = np.array(edges)

    g = Graph(node_number)
    
    for i in range(edge_number):
        g.add_edge(Matrix[i][0],Matrix[i][1])
    

    adjancy_matrix = g.print_matrix()
    
    print('edges are : {} '.format(edges))
    # print(adjancy_matrix)
    print("Adjacency List:")
    x = convert(adjancy_matrix)
    print(x)
    print ("the adjacency list :")
    for i in x:
        print(i, end ="")
        for j in x[i]:
            print(" -> {}".format(j), end ="")
        print()
    print(" ")
    visualize(edges)
    


# ----------------------------------------------------------------------------
# FINDING shorest path
    start,end = random.sample(range(node_number) , 2)
    print('using Breadth-first search to find min route from {} to {} and found :'.format(start,end))
    print(shortest_path(x,start,end))
# ----------------------------------------------------------------------------
# FINDING COMPONENTS  
    my_instance = Graph_struct(node_number)
    for i in range(edge_number):
        my_instance.add_edge(Matrix[i][0],Matrix[i][1])
    conn_comp = my_instance.connected_components()
    print("The connected components are after using Depth-first search :")
    print(conn_comp)
    print('there is total {} components'.format(len(conn_comp)))

if __name__ == '__main__':
    main()