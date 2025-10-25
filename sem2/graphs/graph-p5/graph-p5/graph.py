import random

class Graph:
    def __init__(self, nr_of_vertices=0):
        self.__vertices = set(range(nr_of_vertices))
        self.__edges = {v: set() for v in self.__vertices}
        self.__color = {}

    def get_color(self, vertex):
        if vertex in self.__color:
            return self.__color[vertex]

        return -1

    def set_color(self, vertex, color):
        self.__color.update({vertex: color})

    def add_vertex(self, vertex):
        if vertex in self.__vertices:
            raise ValueError("Vertex already exists.")
        self.__vertices.add(vertex)
        self.__edges[vertex] = set()

    def remove_vertex(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")

        edges = self.__edges[vertex].copy()

        for dest in edges:
            self.remove_edge(vertex, dest)
        del self.__edges[vertex]
        self.__vertices.remove(vertex)

    def add_edge(self, vertex_from, vertex_to):
        if vertex_from not in self.__vertices or vertex_to not in self.__vertices:
            raise ValueError("One or both vertices do not exist.")
        if vertex_to in self.__edges[vertex_from]:
            raise ValueError("Edge already exists.")
        self.__edges[vertex_from].add(vertex_to)
        self.__edges[vertex_to].add(vertex_from)


    def remove_edge(self, vertex_from, vertex_to):
        if not vertex_to in self.__edges[vertex_from]:
            raise ValueError("Edge does not exist.")
        self.__edges[vertex_from].remove(vertex_to)
        self.__edges[vertex_to].remove(vertex_from)

    def get_nr_of_vertices(self):
        return len(self.__vertices)

    def get_nr_of_edges(self):
        nr = 0
        for vertex in self.__edges:
            nr += len(self.__edges[vertex])
        return int(nr / 2)

    def vertices_iterator(self):
        return iter(self.__vertices)

    def edges_iterator(self):
        return iter(self.__edges.values())

    def vertex_edge_iterator(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        return iter(self.__edges[vertex])

    def is_edge(self, vertex_from, vertex_to):
        return vertex_to in self.__edges[vertex_from]

    def is_vertex(self, vertex):
        return vertex in self.__vertices

    def get_degree(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        return len(self.__edges[vertex])

    def copy(self):
        new_graph = Graph()
        new_graph.__vertices = self.__vertices.copy()
        new_graph.__edges = {v: neighbors.copy() for v, neighbors in self.__edges.items()}
        return new_graph

    def generate_random_graph(self, nr_of_vertices, nr_of_edges):
        self.clear_graph()

        if nr_of_edges > nr_of_vertices * (nr_of_vertices - 1):
            raise ValueError("Too many edges.")
        self.__init__(nr_of_vertices)
        edges_added = 0
        while edges_added < nr_of_edges:
            v1, v2 = random.sample(list(self.__vertices), 2)
            if not v1 in self.__edges[v2]:
                self.add_edge(v1, v2)
                edges_added += 1

    def read_graph_from_file(self, file_path):
        self.clear_graph()

        with open(file_path, "r") as file:
            n, m = map(int, file.readline().split())
            self.__init__(n)
            for _ in range(m):
                x, y = map(int, file.readline().split())
                self.add_edge(x, y)

    def save_graph_to_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(f"{self.get_nr_of_vertices()} {self.get_nr_of_edges()}\n")
            for v1 in self.vertices_iterator():
                for v2 in self.vertex_edge_iterator(v1):
                    if v1 < v2:
                        file.write(f"{v1} {v2}\n")

    def clear_graph(self):
        self.__vertices.clear()
        self.__edges.clear()