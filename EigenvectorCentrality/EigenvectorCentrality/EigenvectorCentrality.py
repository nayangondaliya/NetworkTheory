import math 

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

#get total
def getTotal(matrix):
    result = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            result += pow(matrix[row][column], 2)
    return result

#get average
def getAverageVector(matrix, total):
    result = []

    mRow = len(matrix)
    mCol = len(matrix[0])

    result = getMatrix(mRow, mCol, 0)
    root = round(math.sqrt(total), 4)

    for row in range(mRow):
        for col in range(mCol):
            result[row][col] = round(matrix[row][col] / root, 4)
            #result[row][col] = matrix[row][col] / root
    return result 

#get Centrality
def getCentrality(graph, totalVertices, index, iteration):

    oneVector = getMatrix(totalVertices, 1, 1)
    transpose = getTranspose(graph)

    #print("Adjacency Matrix")
    #for row in graph:
    #    print(row)
    
    #print("Transpose Matrix")
    #for row in transpose:
    #    print(row)

    for ite in range(iteration):
        resultVector = multiplyMatrix(transpose, oneVector)
        total = getTotal(resultVector)
        averageVector = getAverageVector(resultVector, total)

        print(f'Iteration {ite + 1} for Graph {index}')
        #for row in averageVector:
        #    for ele in row:
        #        print(ele, end=" ")
        #print()
        print(averageVector)
        oneVector = averageVector.copy()
        print()

vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

totalVertices = 14
graph = generateMatrix("slide.txt", vertices, totalVertices)
getCentrality(graph, totalVertices, 1, 2)

totalVertices = 12
graph = generateMatrix("variant-1.txt", vertices, totalVertices)
getCentrality(graph, totalVertices, 2, 2)

graph = generateMatrix("variant-2.txt", vertices, totalVertices)
getCentrality(graph, totalVertices, 3, 2)

