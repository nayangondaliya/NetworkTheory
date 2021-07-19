class Graph:

	def __init__(self, graph):
		self.graph = graph # residual graph
		self. ROW = len(graph)
		# self.COL = len(gr[0])

	'''Returns true if there is a path from source 's' to sink 't' in
	residual graph. Also fills parent[] to store the path '''
	def BFS(self, s, t, parent):

		# Mark all the vertices as not visited
		visited = [False]*(self.ROW)

		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		# Standard BFS Loop
		while queue:

			# Dequeue a vertex from queue and print it
			u = queue.pop(0)

			# Get all adjacent vertices of the dequeued vertex u
			# If a adjacent has not been visited, then mark it
			# visited and enqueue it
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0:
					# If we find a connection to the sink node,
					# then there is no point in BFS anymore
					# We just have to set its parent and can return true
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
					if ind == t:
						return True

		# We didn't reach sink in BFS starting
		# from source, so return false
		return False
			
	
	# Returns tne maximum flow from s to t in the given graph
	def FordFulkerson(self, source, sink):

		# This array is filled by BFS and to store path
		parent = [-1]*(self.ROW)

		max_flow = 0 # There is no flow initially

		# Augment the flow while there is path from source to sink
		while self.BFS(source, sink, parent) :

			# Find minimum residual capacity of the edges along the
			# path filled by BFS. Or we can say find the maximum flow
			# through the path found.
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Add path flow to overall flow
			max_flow += path_flow

			# update residual capacities of the edges and reverse edges
			# along the path
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow

#get matrix 
def getMatrix(row, column, initialiser):
    matrix = []

    for i in range(row):
        row = []
        for j in range(column):
                row.append(initialiser)
        matrix.append(row)
    return matrix

#read file and generate adjacency matrix
def getAdjacencyMatrix(fileName, vertices, totalVertices):
    matrix = getMatrix(totalVertices, totalVertices, 0)
    file = open(fileName,"r")

    for line in file:
        if line:
            s_list = line.split("=")
            node = s_list[0].strip()
            e_list = s_list[1].split(",")
            node_index = vertices.index(node)

            for edge in e_list:
                edge_l = edge.strip().replace("{", "").replace("}", "").split(":")
                edge_name = edge_l[0]
                    
                edge_index = vertices.index(edge_name)
                matrix[node_index][edge_index] = int(edge_l[1])
                #matrix[edge_index][node_index] = edge_value #un-directed graph
    return matrix

totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
graph = getAdjacencyMatrix("graph-mc.txt", vertices, totalVertices)
search_list = [["e","k"], ["b","k"], ["f","h"], ["a","l"]]

print("Minimum Cut")

for search in search_list:
	graph = getAdjacencyMatrix("graph-mc.txt", vertices, totalVertices)
	g = Graph(graph)
	s_index = vertices.index(search[0])
	t_index = vertices.index(search[1])
	print(f'Minimum Cut between {search[0]} and {search[1]} is : { g.FordFulkerson(s_index, t_index) }')

print()

graph = getAdjacencyMatrix("graph-mf.txt", vertices, totalVertices)
search_list = [["b","l"], ["e","k"], ["e","l"], ["f","d"]]

print("Maximum Flow")

for search in search_list:
	graph = getAdjacencyMatrix("graph-mf.txt", vertices, totalVertices)
	g = Graph(graph)
	s_index = vertices.index(search[0])
	t_index = vertices.index(search[1])
	print(f'Maximum Flow between {search[0]} and {search[1]} is : { g.FordFulkerson(s_index, t_index) }')

