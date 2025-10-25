import random

class Graph:
    def __init__(self, nr_of_vertices=0):
        self.__vertices = set(range(nr_of_vertices))
        self.__outbounds = {v: set() for v in self.__vertices}
        self.__inbounds = {v: set() for v in self.__vertices}
        self.__cost = {}

    def add_vertex(self, vertex):
        if vertex in self.__vertices:
            raise ValueError("Vertex already exists.")
        self.__vertices.add(vertex)
        self.__outbounds[vertex] = set()
        self.__inbounds[vertex] = set()

    def remove_vertex(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        for src in list(self.__inbounds[vertex]):
            self.remove_edge(src, vertex)
        for dest in list(self.__outbounds[vertex]):
            self.remove_edge(vertex, dest)
        del self.__outbounds[vertex]
        del self.__inbounds[vertex]
        self.__vertices.remove(vertex)

    def add_edge(self, vertex_from, vertex_to, edge_cost):
        if vertex_from not in self.__vertices or vertex_to not in self.__vertices:
            raise ValueError("One or both vertices do not exist.")
        if (vertex_from, vertex_to) in self.__cost:
            raise ValueError("Edge already exists.")
        self.__outbounds[vertex_from].add(vertex_to)
        self.__inbounds[vertex_to].add(vertex_from)
        self.__cost[(vertex_from, vertex_to)] = edge_cost

    def remove_edge(self, vertex_from, vertex_to):
        if (vertex_from, vertex_to) not in self.__cost:
            raise ValueError("Edge does not exist.")
        self.__outbounds[vertex_from].remove(vertex_to)
        self.__inbounds[vertex_to].remove(vertex_from)
        del self.__cost[(vertex_from, vertex_to)]

    def get_nr_of_vertices(self):
        return len(self.__vertices)

    def get_nr_of_edges(self):
        return len(self.__cost)

    def vertices_iterator(self):
        return iter(self.__vertices)

    def edges_iterator(self):
        return iter(self.__cost.keys())

    def inbound_iterator(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        return iter(self.__inbounds[vertex])

    def outbound_iterator(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        return iter(self.__outbounds[vertex])

    def is_edge(self, vertex_from, vertex_to):
        return (vertex_from, vertex_to) in self.__cost

    def is_vertex(self, vertex):
        return vertex in self.__vertices

    def get_in_degree(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        return len(self.__inbounds[vertex])

    def get_out_degree(self, vertex):
        if vertex not in self.__vertices:
            raise ValueError("Vertex does not exist.")
        return len(self.__outbounds[vertex])

    def get_cost(self, vertex_from, vertex_to):
        if (vertex_from, vertex_to) not in self.__cost:
            raise ValueError("Edge does not exist.")
        return self.__cost[(vertex_from, vertex_to)]

    def set_cost(self, vertex_from, vertex_to, new_cost):
        if (vertex_from, vertex_to) not in self.__cost:
            raise ValueError("Edge does not exist.")
        self.__cost[(vertex_from, vertex_to)] = new_cost

    def copy(self):
        new_graph = Graph()
        new_graph.__vertices = self.__vertices.copy()
        new_graph.__outbounds = {v: neighbors.copy() for v, neighbors in self.__outbounds.items()}
        new_graph.__inbounds = {v: neighbors.copy() for v, neighbors in self.__inbounds.items()}
        new_graph.__cost = self.__cost.copy()
        return new_graph

    def generate_random_graph(self, nr_of_vertices, nr_of_edges):
        self.clear_graph()

        if nr_of_edges > nr_of_vertices * (nr_of_vertices - 1):
            raise ValueError("Too many edges.")
        self.__init__(nr_of_vertices)
        edges_added = 0
        while edges_added < nr_of_edges:
            v1, v2 = random.sample(list(self.__vertices), 2)
            if (v1, v2) not in self.__cost:
                self.add_edge(v1, v2, random.randint(-3, 9))
                edges_added += 1

    def read_graph_from_file(self, file_path):
        self.clear_graph()

        with open(file_path, "r") as file:
            n, m = map(int, file.readline().split())
            self.__init__(n)
            for _ in range(m):
                x, y, c = map(int, file.readline().split())
                self.add_edge(x, y, c)

    def save_graph_to_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(f"{self.get_nr_of_vertices()} {self.get_nr_of_edges()}\n")
            for (v1, v2), cost in self.__cost.items():
                file.write(f"{v1} {v2} {cost}\n")

    def clear_graph(self):
        self.__vertices.clear()
        self.__outbounds.clear()
        self.__inbounds.clear()
        self.__cost.clear()