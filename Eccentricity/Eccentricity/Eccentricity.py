#generate matrix
def getMatrix(row, column, initialiser):
    matrix = []

    for i in range(row):
            rows = []
            for j in range(column):
                rows.append(initialiser)
            matrix.append(rows)
    return matrix

#generate adjacency matrix
def generateMatrix(fileName, vertices, totalVertices):
    matrix = getMatrix(totalVertices, totalVertices, 0)
    
    file = open(fileName, "r")

    for line in file:
        node_detail = line.split("=")
        node = node_detail[0].strip()
        edge_list = node_detail[1].split(",")
        node_index = vertices.index(node)

        for edge in edge_list:
            edge = edge.strip()
            edge_index = vertices.index(edge)
            
            matrix[node_index][edge_index] = 1
            #matrix[edge_index][node_index] = 1 #graph is undirected

    return matrix

#getting shortest path list
def eccentricity(graph, totalVertices, vertices, source):
    queue = []
    distance = []

    for j in range(totalVertices):
        distance.append(0)

    visitedNodes = []
    queue.append(source)
    nodeIndex = vertices.index(source)

    while len(queue) > 0:
        vertex = queue.pop(0)
        visitedNodes.append(vertex)
        nodeIndex = vertices.index(vertex)
    
        for i in range(totalVertices):
            if graph[nodeIndex][i] == 1 and vertices[i] not in visitedNodes and vertices[i] not in queue:
                distance[i] = distance[nodeIndex] + 1
                queue.append(vertices[i])
    return distance

def getMax(distance):
    max = -1
    for i in range(len(distance)):
        if distance[i] > max:
            max = distance[i]
    return max

totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
graph =  generateMatrix("graph.txt", vertices, totalVertices)
eVertices = ["b", "e", "i", "l"]

for vertex in eVertices:
    distance = eccentricity(graph, totalVertices, vertices, vertex)
    max = getMax(eccentricity(graph, totalVertices, vertices, vertex))
    print("Eccentricity of " + vertex + " is " + str(max))
