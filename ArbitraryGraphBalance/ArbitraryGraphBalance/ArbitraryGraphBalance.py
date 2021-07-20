#get matrix 
def getMatrix(row, column, diagonalInitialiser, initialiser):
    matrix = []

    for i in range(row):
        row = []
        for j in range(column):
                row.append(diagonalInitialiser if i == j else initialiser)
        matrix.append(row)
    return matrix

#read file and generate adjacency matrix
def getAdjacencyMatrix(fileName, vertices, totalVertices):
    matrix = getMatrix(totalVertices, totalVertices, -1, -2)
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
                matrix[edge_index][node_index] = int(edge_l[1]) #un-directed graph

    return matrix

#check structural balance edge
def checkEdge(graph, set, index):

    for node in set:
        if graph[index][node] < 0:
            continue
        elif graph[index][node] == 0:
            return node

    return -1

#check weak structural balance edge
def checkWeakEdge(graph, set, index):

    result = []

    for node in set:
        if graph[index][node] < 0:
            continue
        elif graph[index][node] == 0:
            result.append(0)
        elif graph[index][node] == 1:
            result.append(1)

    return result

#get structural balance
def findStructuralBalance(graph, vertices):
    first = []
    second = []
    
    for i in range(len(graph)):
        for j in range(len(graph)):

            if graph[i][j] > -1 and j not in first and j not in second:
                leftEdge = checkEdge(graph, first, j)
                rightEdge = checkEdge(graph, second, j)

                if leftEdge == -1:
                    first.append(j)
                elif rightEdge == -1:
                    second.append(j)
                else:
                    #print("Conflict occurs " + vertices[j] + " and " + vertices[leftEdge] + " and " + vertices[i])
                    return False
    return True

#get weak structural balance
def findWeakStructuralBalance(graph, vertices):
    resultSets = []

    for i in range(len(graph)):
        for j in range(len(graph)):

            if graph[i][j] > -1:
                
                outputs = []
                for result in resultSets:
                    outputs.append(checkWeakEdge(graph, result, j))
                
                isAdded = False
                isConflict = False

                for index, output in enumerate(outputs):
                    if 0 in output and 1 in output:
                        isConflict = True
                        break

                    if 1 in output:
                        resultSets[index].append(j)
                        isAdded = True
                        break

                if isConflict:
                    #print("Conflict occurs " + vertices[j] + " and " + vertices[leftEdge] + " and " + vertices[i])
                    return False
                else:
                    isExists = False
                    for result in resultSets:
                        if j in result:
                            isExists = True
                            break

                    if not isAdded and not isExists:
                        resultSets.append([j])
    return True

vertices = ['a','b','c','d','e','f','g','h','i','j','k','l']

totalVertices = 9
graph = getAdjacencyMatrix("graph-1.txt", vertices, totalVertices)
print(f'GRAPH 1: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("graph-2.txt", vertices, totalVertices)
print(f'GRAPH 2: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("graph-3.txt", vertices, totalVertices)
print(f'GRAPH 3: {findWeakStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("graph-4.txt", vertices, totalVertices)
print(f'GRAPH 4: {findWeakStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("pratham-1.txt", vertices, totalVertices)
print(f'GRAPH 5: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("pratham-2.txt", vertices, totalVertices)
print(f'GRAPH 6: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("pratham-3.txt", vertices, totalVertices)
print(f'GRAPH 7: {findWeakStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("pratham-4.txt", vertices, totalVertices)
print(f'GRAPH 8: {findWeakStructuralBalance(graph, vertices)}')
print()