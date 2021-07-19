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
    matrix = getMatrix(totalVertices, totalVertices, -1)
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

#add closed triangles
def generateClosedTriangles(triangle, closedTriangle):

    if triangle not in closedTriangle:
        closedTriangle.append(triangle[0] + triangle[1] + triangle[2])
        closedTriangle.append(triangle[1] + triangle[2] + triangle[0])
        closedTriangle.append(triangle[2] + triangle[0] + triangle[1])
        closedTriangle.append(triangle[2] + triangle[1] + triangle[0])
        closedTriangle.append(triangle[0] + triangle[2] + triangle[1])
        closedTriangle.append(triangle[1] + triangle[0] + triangle[2])

#find structural balance
def findStructuralBalance(graph, vertices):
    
    result = True

    closedTriangle = []
    totalVertex = len(graph)
    
    for oEdge in range(totalVertex):
        for iEdge in range(len(graph[oEdge])):
            if oEdge == iEdge:
                continue

            for cEdge in range(len(graph[iEdge])):
                if cEdge == oEdge or graph[iEdge][cEdge] == -1:
                    continue

                if graph[iEdge][cEdge] > -1 and graph[cEdge][oEdge] > -1 and graph[oEdge][iEdge] > -1:
                    generateClosedTriangles(f'{vertices[oEdge]}{vertices[iEdge]}{vertices[cEdge]}', closedTriangle)
                    
                    #SUM MUST BE 3 OR 1
                    sum = graph[oEdge][iEdge] + graph[iEdge][cEdge] + graph[oEdge][cEdge]
                    if sum == 3 or sum == 1:
                        continue
                    else:
                        result = False
                        #print(f'Unbalance at : {vertices[oEdge]}{vertices[iEdge]}{vertices[cEdge]}')
                        return result
    return result

vertices = ['a','b','c','d','e','f','g','h','i','j','k','l']

totalVertices = 6
graph = getAdjacencyMatrix("graph-1.txt", vertices, totalVertices)
print(f'GRAPH 1: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 6
graph = getAdjacencyMatrix("graph-2.txt", vertices, totalVertices)
print(f'GRAPH 2: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("graph-3.txt", vertices, totalVertices)
print(f'GRAPH 3: {findStructuralBalance(graph, vertices)}')
print()

totalVertices = 9
graph = getAdjacencyMatrix("graph-4.txt", vertices, totalVertices)
print(f'GRAPH 4: {findStructuralBalance(graph, vertices)}')
print()
