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

def countPathUptoLength(iteration, firstMatrix, secondMatrix, source, destination):
    result = 0
    
    for iterate in range(0, iteration - 1):
        product = multiplyMatrix(firstMatrix, secondMatrix)
        secondMatrix = product.copy()

    result = secondMatrix[source][destination]
    return result

totalVertices = 12
vertices = ['a','b','c','d','e','f','g','h','i','j','k','l']
searchList = [["g","a",2], ["l","g",5], ["k","a",9], ["h","l",63]]
#searchList = [["d","g",2], ["k","b",3], ["k","a",8], ["h","i",64]]

for search in searchList:
    source = vertices.index(search[0])
    destination = vertices.index(search[1])
    iteration = int(search[2])
    graph = generateMatrix("graph.txt", vertices, totalVertices)
    totalPaths = countPathUptoLength(iteration, graph, graph, source, destination)
    print(f'Paths between {search[0]} and {search[1]} with length {int(search[2])} is: {totalPaths}')