#get matrix 
def getMatrix(row, column, initialiser):
    matrix = []

    for i in range(row):
        row = []
        for j in range(column):
                row.append(initialiser)
        matrix.append(row)
    return matrix

#read file and generate adjacency matrix with STCP
def readFile(fileName, vertices, totalVertices):
    matrix = getMatrix(totalVertices, totalVertices, 0)
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
                edge_type = edge_l[1]
                    
                edge_index = vertices.index(edge_name)
                edge_value = 1 if edge_type == "s" else 2
                matrix[node_index][edge_index] = edge_value
                matrix[edge_index][node_index] = edge_value
    return matrix

#get STCP info
def getNodeSTCP(graph, node, vertices):
    result = False
    
    node_index = vertices.index(node)
    node_edges = graph[node_index]
    s_edges = []

    for edge in range(len(node_edges)):
        if node_edges[edge] == 1:
            s_edges.append(vertices[edge])

    uv_nodes = s_edges.copy()

    for edge in s_edges:
        e_index = vertices.index(edge)

        for uedge in uv_nodes:
            ue_index = vertices.index(uedge)
            
            if graph[e_index][ue_index] == 0 and ue_index != e_index:
                return result

        uv_nodes.remove(edge)

    result = True
    return result

totalVertices = 12
vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
graph = readFile("graph.txt", vertices, totalVertices)
stcp_node = ["b", "a", "k", "f", "g", "h"]

for node in stcp_node:
    result = getNodeSTCP(graph, node, vertices)
    print(f'{node} satisfies STCP : {result}')