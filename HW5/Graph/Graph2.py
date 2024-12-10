from itertools import combinations

class AdjacencyMatrix:
    def __init__(self, adjacency_matrix, vertex_names):
        self.adjacency_matrix = adjacency_matrix
        self.dimension = len(adjacency_matrix)
        self.vertex_names = vertex_names

    def spanning_trees(self):
        all_subgraphs = self.__all_subgraphs()
        spanning_trees = []
        for subgraph in all_subgraphs:
            subgraph_matrix, subgraph_names = self.__create_subgraph_matrix(subgraph)
            edge_count = self.__edge_count(subgraph_matrix)
            is_connected = self.__is_connected(subgraph_matrix)

            print(f"Checking subgraph: {subgraph_names}")
            print(f"Edge count: {edge_count}, Connected: {is_connected}")

            if is_connected and edge_count == self.dimension - 1:
                spanning_trees.append((subgraph_matrix, subgraph_names))
        return spanning_trees

    def __all_subgraphs(self):
        all_combinations = []
        vertices = list(range(self.dimension))
        for r in range(self.dimension, self.dimension + 1):
            all_combinations.extend(combinations(vertices, r))
        return [list(comb) for comb in all_combinations]

    def __create_subgraph_matrix(self, subgraph):
        size = len(subgraph)
        subgraph_matrix = [[0] * size for _ in range(size)]
        subgraph_names = [self.vertex_names[v] for v in subgraph]
        for i, u in enumerate(subgraph):
            for j, v in enumerate(subgraph):
                subgraph_matrix[i][j] = self.adjacency_matrix[u][v]
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

    def __edge_count(self, matrix):
        return sum(sum(row) for row in matrix) // 2

def create_adjacency_matrix(lists):
    vertices = {v: i for i, v in enumerate(set([item for sublist in lists for item in sublist]))}
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]
    vertex_names = [None] * n
    for vertex, index in vertices.items():
        vertex_names[index] = vertex
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
spanning_trees = matrix_graph.spanning_trees()

print("\nSpanning Trees:")
if spanning_trees:
    for idx, (tree, names) in enumerate(spanning_trees):
        print(f"Spanning Tree {idx + 1}:")
        print("Vertices:", names)
        for row in tree:
            print(row)
        print()
else:
    print("No spanning trees found.")
