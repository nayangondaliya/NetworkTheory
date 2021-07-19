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

#get cluster edges
def getClusterTotalEdges(cluster, graph, vertices):
    result = 0
    
    clusterLength = len(cluster)

    for oIndex in range(0, clusterLength):
        for iIndex in range(oIndex + 1, clusterLength):

            oEdgeIndex = vertices.index(cluster[oIndex])
            iEdgeIndex = vertices.index(cluster[iIndex])

            if graph[oEdgeIndex][iEdgeIndex] == 1:
                result += 1

    return result

#get cluster vertices
def getClusterVertices(cluster, graph, vertices):
    result = 0
        
    for edge in cluster:
        edgeIndex = vertices.index(edge)
        connectedEdges = graph[edgeIndex]

        for node in connectedEdges:
            if node == 1:
                result += 1

    return result

#calculate community value
def getCommunityValue(clusters, graph, vertices):
    
    totalEdges = getTotalEdges(graph)
    halfEdges = totalEdges / 2

    #print(f'GRAPH = Total Edges : {totalEdges}, Half Edges : {halfEdges}')

    fc_Edges = getClusterTotalEdges(clusters[0], graph, vertices)
    fc_Vertices = getClusterVertices(clusters[0], graph, vertices)

    #print(f'FC = Edges : {fc_Edges}, Vertices : {fc_Vertices}')

    sc_Edges = getClusterTotalEdges(clusters[1], graph, vertices)
    sc_Vertices = getClusterVertices(clusters[1], graph, vertices)

    #print(f'SC = Edges : {sc_Edges}, Vertices : {sc_Vertices}')

    ####NOTE: ADJUST DECIMAL POINTS AS PER REQUIREMENT####
    f_h_edges = round(fc_Edges / halfEdges, 3)
    f_t_edges = round(pow(fc_Vertices, 2) / pow(totalEdges, 2), 2)
    #f_t_edges = round(pow(fc_Vertices, 2) / pow(totalEdges, 2), 3) SLIDE TESTING

    s_h_edges = round(sc_Edges / halfEdges, 3)
    s_t_edges = round(pow(sc_Vertices, 2) / pow(totalEdges, 2), 2)
    #s_t_edges = round(pow(sc_Vertices, 2) / pow(totalEdges, 2), 3) SLIDE TESTING

    result = round((f_h_edges - f_t_edges) + (s_h_edges - s_t_edges), 2)
    #result = round((f_h_edges - f_t_edges) + (s_h_edges - s_t_edges), 3) SLIDE TESTING

    #print(f'Community value is: {result}')

    return result

#optimiseQ
def performOptimiseQ(iteration, initialCluster, graph, vertices):
    
    firstCluster = initialCluster.copy()
    secondCluster = [x for x in vertices if x not in initialCluster]
    movedVertex = []

    for index in range(0, iteration):
        
        possibleCluster = []
        output = []

        for vertex in vertices:
            
            if vertex in movedVertex:
                continue

            f_cluster = firstCluster.copy()
            s_cluster = secondCluster.copy()

            f_Exist = vertex in firstCluster
            s_Exist = vertex in secondCluster

            if f_Exist:
                f_cluster.remove(vertex)
                s_cluster.append(vertex)
            else:
                s_cluster.remove(vertex)
                f_cluster.append(vertex)

            cluster = [f_cluster, s_cluster]
            possibleCluster.append(cluster)
            output_value = getCommunityValue(cluster, graph, vertices)
            output.append(output_value)
        
        max_out = max(output)
        max_out_index = output.index(max_out)
        movedVertex.append(vertices[max_out_index])

        firstCluster = possibleCluster[max_out_index][0].copy()
        secondCluster = possibleCluster[max_out_index][1].copy()

    return [firstCluster, secondCluster]

vertices = ['a','b','c','d','e','f','g','h','i','j','k']

##################################################################
#slide

#totalVertices = 11
#graph = generateMatrix("slide.txt", vertices, totalVertices)
#clusters = [["a","b","c","d","e","f"],["g","h","i","j","k"]]
#clusters = [["a","b","d","e"],["c","f","g","h","i","j","k"]]
#clusters = [["a","b","f","g","j"],["c","d","e","h","i","k"]]
#print(getCommunityValue(cluster, graph, vertices[0:totalVertices]))

#optimiseQ
#totalIteration = 3
#print(performOptimiseQ(totalIteration, ["a","d","f","h","j"], graph, vertices[0:totalVertices]))

##################################################################
#assignment

#totalVertices = 8
#graph = generateMatrix("graph.txt", vertices, totalVertices)
#clusters = [["a","b","c","d"],["e","f","g","h"]]
#clusters = [["a","b","e","f"],["c","d","g","h"]]
#print(getCommunityValue(cluster, graph, vertices[0:totalVertices]))

#optimiseQ
#totalIteration = 1
#print(performOptimiseQ(totalIteration, ["e","f","h"], graph, vertices[0:totalVertices]))

##################################################################
#pratham

totalVertices = 8
graph = generateMatrix("pratham-g.txt", vertices, totalVertices)
#clusters = [["a","b","e","f"],["c","d","g","h"]]
#clusters = [["a","b","c","e"],["d","f","g","h"]]
#print(getCommunityValue(clusters, graph, vertices[0:totalVertices]))

#optimiseQ
totalIteration = 1
print(performOptimiseQ(totalIteration, ["e","f","g"], graph, vertices[0:totalVertices]))

##################################################################
#for ind, val in enumerate(clusters):
#    print(f'Total edges between cluster {ind + 1} is: {getClusterTotalEdges(val, graph, vertices)}')
#    print(f'Total vertices in cluster {ind + 1} is: {getClusterVertices(val, graph, vertices)}')