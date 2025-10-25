import copy
import queue
from collections import deque
from itertools import count

from graph import Graph


def is_valid_coloring(graph, vertex, color, colors):
    for neighbor in graph.vertex_edge_iterator(vertex): #checks if none of the neighbours have that color
        if colors[neighbor] == color:
            return False
    return True


def backtrack_coloring(graph, colors, vertices, k, index=0): #the backtracking algorithm that sets the colors
    if index == len(vertices): #checks if it set all the vertices to a color
        return True

    vertex = vertices[index] #the current vertex we like to color
    for color in range(k): #tries all the colors on that vertex
        if is_valid_coloring(graph, vertex, color, colors): #checks if the coloring is valid so that the program must continue
            colors[vertex] = color #assigns the color
            if backtrack_coloring(graph, colors, vertices, k, index + 1): #stops the program if a good combination is found
                return True
            colors[vertex] = -1  # resets the vertex color so that it doesent interfere
    return False # no good combination found


def min_vertex_coloring(graph): #the start of the algorithm, it iterates through the colors starting from 1, until it finds the minimum
    n = graph.get_nr_of_vertices() # the number of vertices
    vertices = list(graph.vertices_iterator()) # a list with all the vertices

    for k in range(1, n + 1):# iterates through colors until it finds one
        colors = {v: -1 for v in vertices} # a dictionary that relates a vertex to a color
        if backtrack_coloring(graph, colors, vertices, k): #checks if the color number is valid
            for v in vertices:
                graph.set_color(v, colors[v]) # assigns the found colors
            return k  # Return the number of colors used
    return n  # Worst case: each vertex gets a unique color


def print_coloring(graph):
    for v in sorted(graph.vertices_iterator()):
        print(f"Vertex {v} --> Color {graph.get_color(v)}")


def print_menu():
    print("\nGraph Operations Menu:")
    print("1. Get the number of vertices")
    print("2. Iterate through the set of vertices")
    print("3. Check if an edge exists between two vertices")
    print("4. Get the degree of a vertex")
    print("5. Iterate through edges of a vertex")
    print("9. Add a vertex to the graph")
    print("10. Remove a vertex from the graph")
    print("11. Add an edge to the graph")
    print("12. Remove an edge from the graph")
    print("13. Make a copy of the graph")
    print("14. Read a graph from a file")
    print("15. Write the graph to a file")
    print("16. Generate a random graph")
    print("17. Minimum colors needed")
    print("0. Exit")


def main():
    graph = Graph()
    graph.read_graph_from_file("g1")

    print("G1: ")
    min_colors = min_vertex_coloring(graph)
    print(f"Minimum number of colors needed: {min_colors}")
    print("Coloring:")
    print_coloring(graph)

    print()
    graph.read_graph_from_file("g1")

    print("G1: ")
    min_colors = min_vertex_coloring(graph)
    print(f"Minimum number of colors needed: {min_colors}")
    print("Coloring:")
    print_coloring(graph)

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
                print("Degree:", graph.get_degree(v))
            elif choice == "5":
                v = int(input("Enter vertex: "))
                print("Edges:", list(graph.vertex_edge_iterator(v)))
            elif choice == "9":
                v = int(input("Enter vertex to add: "))
                graph.add_vertex(v)
            elif choice == "10":
                v = int(input("Enter vertex to remove: "))
                graph.remove_vertex(v)
            elif choice == "11":
                v1 = int(input("Enter source vertex: "))
                v2 = int(input("Enter target vertex: "))
                graph.add_edge(v1, v2)
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
                min_colors = min_vertex_coloring(graph)
                print(f"Minimum number of colors needed: {min_colors}")
                print("Coloring:")
                print_coloring(graph)
            elif choice == "p":
                for v1 in graph.vertices_iterator():
                    for v2 in graph.vertex_edge_iterator(v1):
                        if v1 < v2:
                            print(f"{v1} <--> {v2}")
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(ve)

main()