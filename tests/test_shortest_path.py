from src.basic_class import Vertex, Graph
from typing import Dict, Tuple
from src.dijkstra_bellman_ford import dijkstra, bellman_ford, shortest_path

def load_graph(filepath: str) -> Tuple[Graph[str], Dict[str, Vertex[str]]]:
    
    graph = Graph[str]()
    vertices: Dict[str, Vertex[str]] = {}

    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    vertices_index = lines.index('vertices name\n') + 1
    coord_index = lines.index('vertices coordinates\n')
    arcs_index = lines.index('arcs values\n') + 1
    
    for line in lines[vertices_index:coord_index]:
        parts = line.strip().split(maxsplit=1)
        vertex_id, name = parts[0].lstrip('0') or '0', parts[1]
        vertices[vertex_id] = Vertex(name)

    for line in lines[arcs_index:]:
        parts = line.strip().split()
        if len(parts) == 3:
            src_id, dst_id, weight = parts
            graph.add_edge(vertices[src_id], vertices[dst_id], float(weight))

    return graph, vertices

def print_path_table(path: list[Vertex[str]], distance: float, algo_name: str):
    print(f"\n=== {algo_name} ===")
    print(f"{'Index':^7}|{'Station':^30}")
    print("-" * 40)
    for idx, vertex in enumerate(path):
        print(f"{idx:^7}|{vertex.display():^30}")
    print("-" * 40)
    print(f"Total distance: {distance}\n")


def run_example(graph: Graph[str], vertices: Dict[str, Vertex[str]], start_id: str, end_id: str):
    start_vertex = vertices[start_id]
    end_vertex = vertices[end_id]

    # Dijkstra
    dijkstra_distances, dijkstra_predecessors = dijkstra(graph, start_vertex)
    dijkstra_path = shortest_path(end_vertex, dijkstra_predecessors)
    print_path_table(dijkstra_path, dijkstra_distances[end_vertex], "Dijkstra")

    # Bellman-Ford
    bf_distances, bf_predecessors = bellman_ford(graph, start_vertex)
    bf_path = shortest_path(end_vertex, bf_predecessors)
    print_path_table(bf_path, bf_distances[end_vertex], "Bellman-Ford")


# ================================
# Main
# ================================
    
filepath = "datasets/graph_metro_paris.txt"
graph, vertices = load_graph(filepath)

# Example 1 : Gare de l'Est → Gare de Lyon
print("\n Example 1 : Gare de l'Est → Gare de Lyon")
run_example(graph, vertices, start_id="121", end_id="120")

# Example 2 : Crimée → Richard Lenoir
print("\n Example 2 : Crimée → Richard Lenoir")
run_example(graph, vertices, start_id="87", end_id="297")

# Example 3 : Riquet → Abbesses
print("\n Example 3 : Riquet → Abbesses")
run_example(graph, vertices, start_id="300", end_id="0")