import copy
from collections import deque
from itertools import count

from graph import Graph



def dfs(graph : Graph, path, visited):
    if path[-1] not in visited:
        visited.append(path[-1])
    for v in graph.outbound_iterator(path[-1]):
        if v not in path:
            result = dfs(graph, path + [v], visited)
            if not result:
                return False
        else:
            return False
    return True

def is_acyclic(graph : Graph):
    starting_vertices = []
    visited = []
    for v in graph.vertices_iterator():
        if graph.get_in_degree(v) == 0:
            starting_vertices.append(v)

    if not starting_vertices:
        return False

    for v in starting_vertices:
        if not dfs(graph, [v], visited):
            return False

    if len(visited) < graph.get_nr_of_vertices():
        return False

    return True

#does a topological sort on the given graph
def topological_sort(graph : Graph):
    sorted_vertices = []
    layer_count = 0
    in_count = [graph.get_in_degree(v) for v in graph.vertices_iterator()]
    decount_dump = []

    #goes until all vertices are added
    while graph.get_nr_of_vertices() > len(sorted_vertices):
        found = False
        print("In degree count:")
        for v in graph.vertices_iterator():
            print(f"{v}: {in_count[v]}")

        #goes through all the vertices
        for i in range(graph.get_nr_of_vertices()):
            #if its 0, because it s correct for current layer, add it
            if in_count[i] == 0:
                found = True
                sorted_vertices.append(i)
                decount_dump.append(i)
                print("Added " + str(i))

        print()
        if not found:
            print("Not a DAG!")
            return []

        layer_count += 1

        #clear the added vertices
        for dump in decount_dump:
            for v in graph.outbound_iterator(dump):
                in_count[v] -= 1
            in_count[dump] = -1

        decount_dump.clear()

    return sorted_vertices

def highest_cost_path(graph : Graph, vertex_a, vertex_b):
    vertices = topological_sort(graph)
    dist_path = {v: [] for v in vertices}
    dist_path[vertex_a] = [vertex_a]
    dist = {v : float("-inf") for v in vertices}
    dist[vertex_a] = 0
    for key in dist_path:
        print(key, end=": ")
        for element in dist_path[key]:
            print(element, end=", ")
        print("\b\b")
    print()

    #goes through all the vertices
    for vertex in vertices:
        if dist[vertex] == float("-inf"):
            continue

        #end condition
        if vertex == vertex_b:
            break

        #checks best new path from vertex
        for outbound in graph.outbound_iterator(vertex):
            print(f"Checking vertex {vertex} to {outbound}...")
            if dist[outbound] < (dist[vertex] + graph.get_cost(vertex, outbound)):
                print(f"Path {dist_path[vertex] + [outbound]} ({dist[vertex] + graph.get_cost(vertex, outbound)}) better than {dist_path[outbound]} ({dist[outbound]})")

                dist[outbound] = dist[vertex] + graph.get_cost(vertex, outbound)

                dist_path[outbound] = dist_path[vertex] + [outbound]
                for key in dist_path:
                    print(key, end=": ")
                    for element in dist_path[key]:
                        print(element, end=", ")
                    print("\b\b")
            else:
                print(f"Old path {dist_path[outbound]} ({dist[outbound]}) better or equal with {dist_path[vertex] + [outbound]} ({dist[vertex] + graph.get_cost(vertex, outbound)})")
            print()

    print(f"Path to {vertex_b}: {dist_path[vertex_b]}")
    print(f"Path cost to {vertex_b}: {dist[vertex_b]}")

def bt(layer, llist, combs):
    #gives all possible combinations for a certain vector
    if len(llist) == len(layer):
        combs.append(llist.copy())
        return
    for element in layer:
        if not element in llist:
            bt(layer, llist + [element], combs)

def all_topological_orderings(graph : Graph):
    #layers the ordered vertices in layers and creates all the combinations for each of them
    sorted_vertices = []
    in_count = [graph.get_in_degree(v) for v in graph.vertices_iterator()]
    decount_dump = []
    count_layers = [] #the layers

    #same as simple topological ordering
    while graph.get_nr_of_vertices() > len(sorted_vertices):
        found = False
        count_layers.append([])

        for i in range(graph.get_nr_of_vertices()):
            if in_count[i] == 0:
                found = True
                sorted_vertices.append(i)
                decount_dump.append(i)
                count_layers[-1].append(i)

        if not found:
            print("Not a DAG!")
            return []

        for dump in decount_dump:
            for v in graph.outbound_iterator(dump):
                in_count[v] -= 1
            in_count[dump] = -1

        decount_dump.clear()


    #backtracking for all possible combinations
    all_possible_combinations = [[]]
    layer_count = 0
    for layer in count_layers:
        print(f"Adding layer {layer_count} ({layer})")
        combs = []
        bt(layer, [], combs)

        all_comb_nr = len(all_possible_combinations)
        new_all = []
        for comb in combs:
            for i in range(all_comb_nr):
                print(all_possible_combinations[i] + comb)
                new_all.append(all_possible_combinations[i] + comb)
        all_possible_combinations = new_all
        layer_count += 1

def print_menu():
    print("\nGraph Operations Menu:")
    print("1. Get the number of vertices")
    print("2. Iterate through the set of vertices")
    print("3. Check if an edge exists between two vertices")
    print("4. Get the in-degree and out-degree of a vertex")
    print("5. Iterate through outbound edges of a vertex")
    print("6. Iterate through inbound edges of a vertex")
    print("7. Retrieve the cost of an edge")
    print("8. Modify the cost of an edge")
    print("9. Add a vertex to the graph")
    print("10. Remove a vertex from the graph")
    print("11. Add an edge to the graph")
    print("12. Remove an edge from the graph")
    print("13. Make a copy of the graph")
    print("14. Read a graph from a file")
    print("15. Write the graph to a file")
    print("16. Generate a random graph")
    print("17. Highest cost path")
    print("18. Topological sort")
    print("19. All topological orderings")
    print("0. Exit")

def main():
    graph = Graph()
    graph.read_graph_from_file("g2.txt")

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                print("Number of vertices:", graph.get_nr_of_vertices())
            elif choice == "2":
                print("Vertices:", list(graph.vertices_iterator()))
            elif choice == "3":
                v1 = int(input("Enter source vertex: "))
                v2 = int(input("Enter target vertex: "))
                print("Edge exists:" if graph.is_edge(v1, v2) else "No edge found")
            elif choice == "4":
                v = int(input("Enter vertex: "))
                print("In-degree:", graph.get_in_degree(v))
                print("Out-degree:", graph.get_out_degree(v))
            elif choice == "5":
                v = int(input("Enter vertex: "))
                print("Outbound edges:", list(graph.outbound_iterator(v)))
            elif choice == "6":
                v = int(input("Enter vertex: "))
                print("Inbound edges:", list(graph.inbound_iterator(v)))
            elif choice == "7":
                v1 = int(input("Enter source vertex: "))
                v2 = int(input("Enter target vertex: "))
                print("Cost:", graph.get_cost(v1, v2))
            elif choice == "8":
                v1 = int(input("Enter source vertex: "))
                v2 = int(input("Enter target vertex: "))
                new_cost = int(input("Enter new cost: "))
                graph.set_cost(v1, v2, new_cost)
            elif choice == "9":
                v = int(input("Enter vertex to add: "))
                graph.add_vertex(v)
            elif choice == "10":
                v = int(input("Enter vertex to remove: "))
                graph.remove_vertex(v)
            elif choice == "11":
                v1 = int(input("Enter source vertex: "))
                v2 = int(input("Enter target vertex: "))
                cost = int(input("Enter cost: "))
                graph.add_edge(v1, v2, cost)
            elif choice == "12":
                v1 = int(input("Enter source vertex: "))
                v2 = int(input("Enter target vertex: "))
                graph.remove_edge(v1, v2)
            elif choice == "13":
                copy_graph = graph.copy()
                print("Graph copied successfully.")
            elif choice == "14":
                filename = input("Enter file name: ")
                graph.read_graph_from_file(filename)
                print("Graph loaded from file.")
            elif choice == "15":
                filename = "output.txt"
                graph.save_graph_to_file(filename)
                print("Graph saved to file.")
            elif choice == "16":
                vertices = int(input("Enter number of vertices: "))
                edges = int(input("Enter number of edges: "))
                graph.generate_random_graph(vertices, edges)
                print("Random graph generated.")
            elif choice == "17":
                starting_vertice = int(input("Enter starting vertex: "))
                ending_vertice = int(input("Enter ending vertex: "))
                highest_cost_path(graph, starting_vertice, ending_vertice)
            elif choice == "18":
                print(topological_sort(graph))
            elif choice == "19":
                all_topological_orderings(graph)

            elif choice == "p":
                for vertex in graph.vertices_iterator():
                    print(f"{vertex} ->", end="")
                    for edge in graph.outbound_iterator(vertex):
                        print(f" {edge}", end=",")
                    print("\b")
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(ve)

main()
