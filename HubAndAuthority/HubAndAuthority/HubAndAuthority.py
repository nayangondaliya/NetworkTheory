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
            #matrix[edge_index][node_index] = 1 #graph is undirected
    return matrix

#get Transpose
def getTranspose(graph):
    tRows = len(graph)
    tCols = len(graph[0])

    matrix = getMatrix(tRows, tCols, 0)
    
    for row in range(tRows):
        for col in range(tCols):
            matrix[row][col] = graph[col][row]
    return matrix

#multiply matrix
def multiplyMatrix(first, second):
    result = []

    if len(first) == 0 or len(second) == 0:
        return result

    if len(first[0]) == 0 or len(second[0]) == 0:
        return result

    fRowLength = len(first)
    fColLength = len(first[0])
    sRowLength = len(second)
    sColLength = len(second[0])

    result = getMatrix(fRowLength, sColLength, 0)

    for fRow in range(fRowLength):
        for sColumn in range(sColLength):
            for fColumn in range(fColLength):
                result[fRow][sColumn] += first[fRow][fColumn] * second[fColumn][sColumn]
            #result[fRow][sColumn] = round(result[fRow][sColumn], 1)
    return result

totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
graph = generateMatrix("graph.txt", vertices, totalVertices)
graph = generateMatrix("pratham-g.txt", vertices, totalVertices)

transpose = getTranspose(graph)
oneVector = getMatrix(totalVertices, 1, 1)
authorityVector = multiplyMatrix(transpose, oneVector)
hubVector = multiplyMatrix(graph, authorityVector)

print("Authority Score:")
for row in range(len(authorityVector)):
    print(f'{vertices[row]} has authority score of {authorityVector[row]}')

print()

print("Hub Score:")
for row in range(len(hubVector)):
    print(f'{vertices[row]} has hub score of {hubVector[row]}')

