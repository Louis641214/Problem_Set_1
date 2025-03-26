from basic_class import Vertex, Graph
from typing import Dict
from djikstra import djikstra, shortest_path

def load_graph(filepath: str) -> Graph[str]:
    
    graph = Graph[str]()
    vertices: Dict[str, Vertex[str]] = {}

    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    vertices_index = lines.index('noms sommets\n') + 1
    coord_index = lines.index('coord sommets\n')
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

filepath = "graph_subway_paris.txt"
graph, vertices = load_graph(filepath)

start_vertex = vertices["87"]  # Crimée
end_vertex = vertices["297"]    # Richard Lenoir

distances, predecessors = djikstra(graph, start_vertex)
path = shortest_path(end_vertex, predecessors)

print("Shortest path:", [vertex.display() for vertex in path])
print("Distance :", distances[end_vertex])