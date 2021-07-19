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
        if line:
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

#get all path list
def printAllPathsUtil(source, destination, visited, path, graph, pathList):
 
        # Mark the current node as visited and store in path
        visited[source]= True
        path.append(source)
 
        # If current vertex is same as destination, then print
        # current path[]
        if source == destination:
            pathList.append(path.copy())
            #print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in range(len(graph[source])):
                if visited[i]== False and graph[source][i] == 1:
                    printAllPathsUtil(i, destination, visited, path, graph, pathList)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[source]= False

# Prints all paths from 's' to 'd'
def printAllPaths(source, destination, totalVertices, graph, pathList):
 
        # Mark all the vertices as not visited
        visited =[False]*totalVertices
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        printAllPathsUtil(source, destination, visited, path, graph, pathList)

def printAllPath(source, destination, fNode, sNode, pathList, vertices, shortestDist):
    
    #print() #For Space
    #first index = non-edge
    #second index = with edge
    result = [0, 0]

    for path in pathList:
        if (len(path) - 1) == shortestDist:
            s_index = vertices.index(source)
            d_index = vertices.index(destination)
            fn_index = vertices.index(fNode)
            sn_index = vertices.index(sNode)
            
            is_source_first = path[0] == s_index
            is_dest_last = path[len(path) - 1] == d_index
            
            if is_source_first and is_dest_last:
                result[0] += 1

                #for node in path:
                #    print(vertices[node], end=" ")
                #print()

                if fn_index in path and sn_index in path:
                    is_edge = path.index(sn_index) - path.index(fn_index) == 1

                    if is_edge:
                        result[1] += 1
    #print() #For Space
    return result

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

#find betweenness for searches
def findBetweenness(searchList, graph, totalVertices, vertices, isPrint = False):
    totalBetweenness = 0

    for search in searchList:
        pathList = []
        dist_graph = graph.copy()
        shortestDist = 0

        s_index = vertices.index(search[0])
        d_index = vertices.index(search[1])

        while dist_graph[s_index][d_index] == 0:
            shortestDist += 1
            dist_graph = multiplyMatrix(graph, dist_graph)
                
        printAllPaths(s_index, d_index, totalVertices, graph, pathList)
        #print(f'Possible path between {search[0]} and {search[1]} using edge {search[2]} <=> {search[3]} is following:')
        result = printAllPath(search[0], search[1], search[2], search[3], pathList, vertices, shortestDist + 1)
        #print(f'Total Available Shortest Paths With Distance : {shortestDist + 1} is {result[0]}')
        #print(f'Total Shortest Paths Not Using Edge {search[2]} <=> {search[3]} are: {result[0] - result[1]}')
        #print(f'Total Shortest Paths Using Edge {search[2]} <=> {search[3]} are: {result[1]}')

        if result[0] > 0:
            totalBetweenness += round(result[1] / result[0], 2)
            if isPrint:
                print(f'Betweenness of {search[0]} and {search[1]} using edge {search[2]} <=> {search[3]} is : {round(result[1] / result[0], 2)}')
        else:
            if isPrint:
                print(f'Betweenness of {search[0]} and {search[1]} using edge {search[2]} <=> {search[3]} is : -1')
        
        if isPrint:
            print()
    return round(totalBetweenness, 2)

#get possible edges
def getPossibleEdges(fNode, sNode):
    searchList = []

    for mVertex in vertices:
        for iVertex in vertices:
            if mVertex != iVertex:
                searchList.append([mVertex, iVertex, fNode, sNode])
    
    return searchList

#get Graph betweenness
def getGraphBetweenness(edges, graph, totalVertices, vertices):
    betweenness = []
    
    for edge in edges:
        searchList = getPossibleEdges(edge[0], edge[1])
        betweenness.append(findBetweenness(searchList, graph, totalVertices, vertices))
    
    for index in range(len(edges)):
        print(f'Betweenness of graph using edge {edges[index][0]} <=> {edges[index][1]} is : {betweenness[index]}')
        print()

totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
graph =  generateMatrix("graph.txt", vertices, totalVertices)

#Search for particular nodes
#searchList = [["i","d","f","g"], ["a","h","f","g"]]
#findBetweenness(searchList, graph, totalVertices, vertices, True)

#Search for whole graph
edges = [["f", "g"], ["b", "c"]]
getGraphBetweenness(edges, graph, totalVertices, vertices)

#Second Graph
#graph =  generateMatrix("pratham-g.txt", vertices, totalVertices)

##Search for particular nodes
#searchList = [["i","d","f","g"], ["e","b","a","b"]]
#findBetweenness(searchList, graph, totalVertices, vertices, True)

##Search for whole graph
#edges = [["f", "g"], ["g", "l"]]
#getGraphBetweenness(edges, graph, totalVertices, vertices)