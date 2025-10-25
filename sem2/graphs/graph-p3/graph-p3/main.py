import copy

from graph import Graph

inf = float('inf')

#it fixes the path when we can reach a node after not being able to do that before
def fix_path(path):
    for i in range(len(path)):
        for j in range(len(path)):
            if -1 in path[i][j]:
                first = path[i][j].index(-1)
                last = len(path[i][j]) - 1 - path[i][j][::-1].index(-1)

                if last != len(path[i][j]) - 1:
                    for k in range(first, last + 1):
                        vertex_to_search = path[i][j][last + 1]
                        path[i][j][k] = path[i][vertex_to_search][k]

#using the matrix multiplication algorithm
#creates a new matrix that contains the lowest cost walk
#in edge_number edges
def matrix_multiply(l, edge_number, n, paths):
    for i in range(n):
        for j in range(n):
            min_vertex_destination = -1
            minn = inf
            for k in range(n):
                num = l[0][k][j] + l[edge_number - 1][i][k]
                if num < minn:
                    minn = num
                    min_vertex_destination = k
            l[edge_number][i][j] = minn
            if paths[i][j][-1] != min_vertex_destination:
                paths[i][j].append(min_vertex_destination)

            if i == j and l[edge_number][i][i] < 0:
                print("Negative cycle detected! " + str(i) + " " + str(j))
                exit(1)

    fix_path(paths)

#sets up and prints the matrices
#it also calculates all the matrices up to m edges
def matrix_multiplication_algorithm(graph, A, B):
    n = graph.get_nr_of_vertices()
    m = graph.get_nr_of_edges()

    empty_matrix = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        empty_matrix[i][i] = 0
    l = [copy.deepcopy(empty_matrix) for _ in range(m)]
    paths = [[[j]for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if graph.is_edge(i,j):
                l[0][i][j] = graph.get_cost(i,j)
                paths[i][j].append(i)

    for row in l[0]:
        for val in row:
            print(f"{val:3}", end=" ")
        print()
    print()

    for i in range(1, m):
        matrix_multiply(l, i, n, paths)

        for row in l[i]:
            for val in row:
                print(f"{val:3}", end=" ")
            print()
        print()

    for row in paths:
        for val in row:
            print(f"{str(val):3}", end=" ")
        print()
    print()

    print("The shortest path from " + str(A) + " to " + str(B) + " takes " + str(l[m-1][A][B]))
    print("The shortest path from " + str(A) + " to " + str(B) + " is " + str(paths[A][B]))




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
    print("0. Exit")

def main():
    graph = Graph()

    graph.read_graph_from_file("g1.txt")
    matrix_multiplication_algorithm(graph, 1,2)

    graph.read_graph_from_file("g2.txt")
    matrix_multiplication_algorithm(graph, 0, 6)

    graph.read_graph_from_file("g3.txt")
    matrix_multiplication_algorithm(graph, 4, 9)

    #graph.generate_random_graph(20, 40)
    #matrix_multiplication_algorithm(graph, 0, 15)

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
                matrix_multiplication_algorithm(graph, starting_vertice, ending_vertice)

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
