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

#get outDegree
def getOutDegree(graph, vertices, totalVertices):
    outDegree = {}

    for node in range(totalVertices):
        cVertex = vertices[node]
        outDegree[cVertex] = 0
        for vertex in range(totalVertices):
            if graph[node][vertex] == 1:
                outDegree[cVertex] += 1
    return outDegree

#get inDegree
def getInDegree(graph, vertices, totalVertices):
    inDegree = {}

    for vertex in vertices:
        inDegree[vertex] = 0

    for node in range(totalVertices):
        for vertex in range(totalVertices):
            if graph[node][vertex] == 1:
                inDegree[vertices[vertex]] += 1
    return inDegree


totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
graph = generateMatrix("graph.txt", vertices, totalVertices)
outDegree = getOutDegree(graph, vertices, totalVertices)

for key in outDegree:
    print(f'Out Degree of {key} is: {outDegree[key]}')

print()

inDegree = getInDegree(graph, vertices, totalVertices)

for key in outDegree:
    print(f'In Degree of {key} is: {inDegree[key]}')