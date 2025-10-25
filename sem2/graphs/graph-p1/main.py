from graph import Graph

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
