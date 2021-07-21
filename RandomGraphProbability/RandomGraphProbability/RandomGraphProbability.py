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

#get total edges in graph
def getTotalEdges(graph):
    result = 0

    for oIndex in range(len(graph)):
        for iIndex in range(len(graph[oIndex])):
            if graph[oIndex][iIndex] == 1:
                result += 1

    return result

#get factorial
def factorial(number):
   if number < 0:
       return number

   if number == 1:
       return number
   else:
       return number*factorial(number-1)

#get probability
def GetProbability(graph, roundOff, model, m, n, p):
    result = 0
    
    totalEdges = getTotalEdges(graph)
    halfEdges = totalEdges / 2
    possibleEdges = ((n * (n - 1)) / 2)

    if model == 1: #G(N,M) MODEL
        if halfEdges == m:
            firstF = factorial(possibleEdges)
            secondF = factorial(m)
            thirdF = factorial(possibleEdges - m)
            result = round(1 / (firstF / (secondF * thirdF)), roundOff)
    elif model == 2: #G(N,P) MODEL
        proPower = pow(p, halfEdges)
        nProPower = pow(1 - p, possibleEdges - halfEdges)
        result = round(proPower * nProPower, roundOff)

    return result

totalVertices = 6
vertices = ['a','b','c','d','e','f','g','h','i','j','k','l']
GNM = 1
GNP = 2

m = 6
n = 6
p = 0.3
roundOff = 6

graph = generateMatrix("graph.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 1: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("graph-1.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 2: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("graph-2.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 3: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("graph-3.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 4: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("pratham-1.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 5: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("pratham-2.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 6: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("pratham-3.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 7: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()

graph = generateMatrix("pratham-4.txt", vertices[0:totalVertices], totalVertices)
print(f'GRAPH 8: G(N,M) = {GetProbability(graph, roundOff, GNM, m, n, p)} AND G(N,P) = {GetProbability(graph, roundOff, GNP, m, n, p)}')
print()