from itertools import combinations

class AdjacencyMatrix:
    def __init__(self, adjacency_matrix, vertex_names):
        self.adjacency_matrix = adjacency_matrix
        self.dimension = len(self.adjacency_matrix)
        self.vertex_names = vertex_names

    def connected_subgraph(self):
        subgraphs = self.__all_subgraphs()
        connected_subgraphs = []
        for subgraph in subgraphs:
            subgraph_matrix, subgraph_names = self.__create_subgraph_matrix(subgraph)
            if self.__is_connected(subgraph_matrix):
                connected_subgraphs.append((subgraph_matrix, subgraph_names))
        return connected_subgraphs

    def __all_subgraphs(self):
        all_combinations = []
        vertices = list(range(self.dimension))
        for r in range(1, len(vertices) + 1):
            all_combinations.extend(combinations(vertices, r))
        return [list(comb) for comb in all_combinations]

    def __create_subgraph_matrix(self, subgraph):
        subgraph_matrix = [[0] * len(subgraph) for _ in range(len(subgraph))]
        subgraph_names = [self.vertex_names[v] for v in subgraph]
        for i, u in enumerate(subgraph):
            for j, v in enumerate(subgraph):
                if self.adjacency_matrix[u][v] == 1:
                    subgraph_matrix[i][j] = 1
        return subgraph_matrix, subgraph_names

    def __is_connected(self, matrix):
        visited = [False] * len(matrix)
        self.__dfs(0, matrix, visited)
        return all(visited)

    def __dfs(self, vertex, matrix, visited):
        visited[vertex] = True
        for i in range(len(matrix)):
            if matrix[vertex][i] == 1 and not visited[i]:
                self.__dfs(i, matrix, visited)

def create_adjacency_matrix(lists):
    vertices = {v: i for i, v in enumerate(set([item for sublist in lists for item in sublist]))}
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]
    vertex_names = list(vertices.keys())
    for lst in lists:
        i = vertices[lst[0]]
        for vertex in lst[1:]:
            j = vertices[vertex]
            matrix[i][j] = 1
            matrix[j][i] = 1
    return matrix, vertex_names

lists = [
    ["A", "B", "C"],
    ["B", "A", "E", "C"],
    ["C", "B", "A", "D"],
    ["D", "C", "E"],
    ["E", "D", "B"]
]

adjacency_matrix, vertex_names = create_adjacency_matrix(lists)
matrix_graph = AdjacencyMatrix(adjacency_matrix, vertex_names)
connected_subgraphs = matrix_graph.connected_subgraph()

for subgraph_matrix, subgraph_names in connected_subgraphs:
    print("Vertices:", subgraph_names)
    for row in subgraph_matrix:
        print(row)
    print()
