import queue

from graph import Graph

#returns the path from one node to another using a traversal history dictionary
def get_path(next, starting, ending):
    path = [starting]
    current = starting
    while current != ending:
        if not current in next.keys():
            return "No path available!"
        path.append(next[current])
        current = next[current]

    return path

#basic reverse bfs algorithm, it searches for the inbound edges instead of the outbound ones
def bfs(graph, starting_vertex, ending_vertex):
    dist = {}
    dist_count = 0
    current_vertex = ending_vertex
    next = {}
    visited_set = set()
    visiting_queue = queue.Queue()

    visited_set.add(ending_vertex)
    visiting_queue.put(current_vertex)

    while current_vertex != starting_vertex and not visiting_queue.empty():
        current_vertex = visiting_queue.get()
        dist[current_vertex] = dist_count

        for edge in graph.inbound_iterator(current_vertex):
            if edge not in visited_set:
                visited_set.add(edge)
                visiting_queue.put(edge)
                next[edge] = current_vertex

        dist_count += 1

    return get_path(next, starting_vertex, ending_vertex)

#the main function that runs all the specified functionalities
def main():
    graph = Graph()

    graph.read_graph_from_file("input.txt")
    for i in range(2):
        starting_vertex = int(input("Starting vertex: "))
        ending_vertex = int(input("Ending vertex: "))
        print(bfs(graph, starting_vertex, ending_vertex), end="\n\n")

    files = ["graph1k.txt", "graph10k.txt", "graph100k.txt"]
    for file in files:
        graph.read_graph_from_file(file)
        starting_vertex = 1
        ending_vertex = 100
        print(file + " going from 1 to 100")
        print(bfs(graph, starting_vertex, ending_vertex))

        starting_vertex = 100
        ending_vertex = 1
        print(file + " going from 100 to 1")
        print(bfs(graph, starting_vertex, ending_vertex), end="\n\n")

if __name__ == '__main__':
    main()