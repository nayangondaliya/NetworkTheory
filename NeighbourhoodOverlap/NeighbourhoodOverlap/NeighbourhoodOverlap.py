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

#get node connection
def getConnection(graph, node, relatenode, vertices):
    result = []

    edges = graph[vertices.index(node)]
    relateNodeIndex = vertices.index(relatenode)

    if edges[relateNodeIndex] == 0:
        return result

    for edge in range(len(edges)):
        if edges[edge] == 1 and edge != relateNodeIndex:
            result.append(vertices[edge])

    return result


vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

#totalVertices = 12
#graph = generateMatrix("graph.txt", vertices, totalVertices)
#overlap = [{"e":"f"}, {"g":"l"}, {"j":"k"}, {"f":"g"}]

totalVertices = 14
graph = generateMatrix("slide.txt", vertices, totalVertices)
overlap = [{"a":"b"}, {"l":"m"}, {"c":"i"}, {"d":"e"}]

for pair in overlap:
    for key in pair:
        f_edges = getConnection(graph, key, pair[key], vertices)
        s_edges = getConnection(graph, pair[key], key, vertices)
        common = list(set(f_edges).intersection(s_edges))
        c_common = len(common)
        t_edges = len(f_edges) + len(s_edges)

        if c_common > 0 or t_edges > 0:
            c_overlap = round(c_common / (t_edges - c_common), 2)
            print(f'Overlap between {key} and {pair[key]} is: {c_overlap}')
        else:
            print(f'Overlap between {key} and {pair[key]} is: -1')

        