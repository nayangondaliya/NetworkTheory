import numpy
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

#multiply one variable
def multiplyOneVariable(matrix, value):
    tRows = len(matrix)
    tCols = len(matrix[0])

    result = getMatrix(tRows, tCols, 0)
    
    for row in range(tRows):
        for col in range(tCols):
            result[row][col] = value * matrix[row][col]
    return result

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

#get Diagonal Matrix
def getDiagonal(row, column, outDegree, vertices):
    matrix =  getMatrix(row, column, 0)

    for key in outDegree:
        index = vertices.index(key)
        matrix[index][index] = outDegree[key] if outDegree[key] > 0 else 1
    return matrix

#subtract matrix
def subtractMatrix(first, second):
    tRows = len(first)
    tCols = len(first[0])

    result = getMatrix(tRows, tCols, 0)
    
    for row in range(tRows):
        for col in range(tCols):
            result[row][col] = first[row][col] - second[row][col]
    return result

#round matrix
def roundMatrix(matrix, r):

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = round(matrix[row][col], r)
    return matrix

totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
alpha = 0.6

graph = generateMatrix("graph.txt", vertices, totalVertices)
transpose = getTranspose(graph)

outDegree = getOutDegree(graph, vertices, totalVertices)
diagonal = getDiagonal(totalVertices, totalVertices, outDegree, vertices)

#multiply transpose with alpha
mult_transpose = multiplyOneVariable(transpose, alpha)

#subtract matrix
sub_matrix = subtractMatrix(diagonal, mult_transpose)

#inverse matrix
inv_matrix = numpy.linalg.inv(sub_matrix)

#multiply inverse with diagonal
mult_matrix = multiplyMatrix(diagonal, inv_matrix)

#multiply multiplied matrix with one vector
oneVector = getMatrix(totalVertices, 1, 1)
f_matrix = multiplyMatrix(mult_matrix, oneVector)

print("Decimal Round Up to 4")
r_f_matrix = roundMatrix(f_matrix, 4)
print(r_f_matrix)

print()

print("Decimal Round Up to 2")
r_t_matrix = roundMatrix(f_matrix, 2)
print(r_t_matrix)