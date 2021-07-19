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

#calculate node clustering coefficient
def countNodeCoefficient(node, graph, vertices):
    result = 0
    
    nodeIndex = vertices.index(node)
    connected_edges = graph[nodeIndex]
    edges = []

    for edge, val in enumerate(connected_edges):
        if val == 1:
            edges.append(edge)

    edgeConnection = 0
    totalEdges = len(edges)

    for oIndex in range(0, totalEdges):
        for iIndex in range(oIndex, totalEdges):
            if edges[oIndex] == edges[iIndex]:
                continue
            else:
                if graph[edges[oIndex]][edges[iIndex]] == 1:
                    edgeConnection += 1
    
    if totalEdges > 1:
        result = round((2 * edgeConnection) / (totalEdges * (totalEdges - 1)), 2)

    return result

#add closed triangles
def generateClosedTriangles(triangle, closedTriangle):

    if triangle not in closedTriangle:
        closedTriangle.append(triangle[0] + triangle[1] + triangle[2])
        closedTriangle.append(triangle[1] + triangle[2] + triangle[0])
        closedTriangle.append(triangle[2] + triangle[0] + triangle[1])
        closedTriangle.append(triangle[2] + triangle[1] + triangle[0])
        closedTriangle.append(triangle[0] + triangle[2] + triangle[1])
        closedTriangle.append(triangle[1] + triangle[0] + triangle[2])

#add open triangles
def generateOpenTriangles(triangle, openTriangle):
    
    if triangle not in openTriangle:
        openTriangle.append(triangle[0] + triangle[1] + triangle[2])
        openTriangle.append(triangle[2] + triangle[1] + triangle[0])

#find open and close triangle
def getGlobalCoefficient(graph, vertices):
    result = 0

    openTriangle = []
    closedTriangle = []

    totalVertex = len(graph)
    
    for oEdge in range(totalVertex):
        for iEdge in range(len(graph[oEdge])):
            if oEdge == iEdge:
                continue

            for cEdge in range(len(graph[iEdge])):
                if cEdge == oEdge or graph[iEdge][cEdge] == 0:
                    continue

                if graph[iEdge][cEdge] == 1 and graph[cEdge][oEdge] == 1 and graph[oEdge][iEdge] == 1:
                    generateClosedTriangles(f'{vertices[oEdge]}{vertices[iEdge]}{vertices[cEdge]}', closedTriangle)
                elif graph[iEdge][cEdge] == 1 and graph[cEdge][oEdge] == 0 and graph[oEdge][iEdge] == 1:
                    generateOpenTriangles(f'{vertices[oEdge]}{vertices[iEdge]}{vertices[cEdge]}', openTriangle)

    totalTriangle = len(openTriangle) + len(closedTriangle)
    result = round(len(closedTriangle) / totalTriangle, 2)
    return result

totalVertices = 12
vertices = ['a','b','c','d','e','f','g','h','i','j','k','l']
graph = generateMatrix("pratham.txt", vertices, totalVertices)
#searchList = ["a", "k", "e"]
searchList = ["g", "f", "d"]

for node in searchList:
    print(f'Clustering coefficient of {node} is: {countNodeCoefficient(node, graph, vertices)}')

print(f'Global coefficient is: {getGlobalCoefficient(graph, vertices)}')
