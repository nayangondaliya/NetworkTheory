#get matrix 
def getMatrix(row, column, initialiser):
    matrix = []

    for i in range(row):
        row = []
        for j in range(column):
                row.append(initialiser)
        matrix.append(row)
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
            matrix[edge_index][node_index] = 1 #graph is undirected
    return matrix

#get degree of vertices
def getDegreeDistribution(graph, degreeCounter, totalVertices):
    result = {}
    degreeList = []
    degrees = []

    for degree in range(0, degreeCounter + 1):
        degrees.append(degree)

    for index in range(totalVertices):
        edges = graph[index]
        connection = 0

        for edge in edges:
            connection += 1 if edge == 1 else 0

        degreeList.append(connection)

    for degree in degrees:
        occurences = degreeList.count(degree)
        result[degree] = round(occurences / totalVertices, 2)

    return result

totalVertices = 12
vertices = ['a','b','c','d','e','f','g','h','i','j','k','l']
graph = generateMatrix("graph.txt", vertices, totalVertices)
degreeDist = getDegreeDistribution(graph, 10, totalVertices)

for degree in degreeDist:
    print(f'G1: Frequency of degree {degree} is : {degreeDist[degree]}')

print()

graph = generateMatrix("pruthvi.txt", vertices, totalVertices)
degreeDist = getDegreeDistribution(graph, 10, totalVertices)

for degree in degreeDist:
    print(f'G2: Frequency of degree {degree} is : {degreeDist[degree]}')