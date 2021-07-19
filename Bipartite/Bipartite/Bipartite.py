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
            matrix[edge_index][node_index] = 1 #graph is undirected
    return matrix

def checkEdge(graph, set, index):
    for node in set:
        if graph[index][node] == 1:
            return node
    return -1

def checkBipartite(graph, totalVertices, vertices):
    left = []
    right = []
    
    for i in range(totalVertices):
        leftEdge = checkEdge(graph, left, i)
        rightEdge = checkEdge(graph, right, i)

        if leftEdge == -1:
            left.append(i)
        elif rightEdge == -1:
            right.append(i)
        else:
            print("Conflict occurs " + vertices[i] + " and " + vertices[leftEdge] + " and " + vertices[rightEdge])
            return -1
    return 0

totalVertices = 18
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"]
graph =  generateMatrix("graph.txt", vertices, totalVertices)
print(checkBipartite(graph, totalVertices, vertices))

graph =  generateMatrix("graph-1.txt", vertices, totalVertices)
print(checkBipartite(graph, totalVertices, vertices))