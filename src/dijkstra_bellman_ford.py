import itertools
from typing import Dict
from .basic_class import T, Vertex, Graph, Tuple, List

import heapq

def dijkstra(g: Graph[T], v: Vertex[T]) -> Tuple[Dict[Vertex[T], float], Dict[Vertex[T], Vertex[T] | None]]:

    distances: Dict[Vertex[T], float] = {vertex: float('inf') for vertex in g.adjacency}
    distances[v] = 0

    heap: List[Tuple[float, int, Vertex[T]]] = [(0, 0, v)]
    counter = itertools.count(1)

    predecessors: Dict[Vertex[T], Vertex[T] | None] = {vertex: None for vertex in g.adjacency}

    while heap:

        current_distance, _, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for vertex, distance in g.adjacency[current_vertex]:
            new_distance = current_distance + distance
            if new_distance < distances[vertex]:
                distances[vertex]=new_distance
                heapq.heappush(heap, (new_distance, next(counter), vertex))
                predecessors[vertex] = current_vertex
            
    return distances, predecessors

def bellman_ford(g: Graph[T], v: Vertex[T]) -> Tuple[Dict[Vertex[T], float], Dict[Vertex[T], Vertex[T] | None]]:
    
    distances: Dict[Vertex[T], float] = {vertex: float('inf') for vertex in g.adjacency}
    distances[v] = 0

    predecessors: Dict[Vertex[T], Vertex[T] | None] = {vertex: None for vertex in g.adjacency}

    num_vertices = len(g.adjacency)

    for _ in range(num_vertices):
        for u in g.adjacency:
            for v, weight in g.adjacency[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Detection of negative weight cycles
    for u in g.adjacency:
        for v, weight in g.adjacency[u]:
            if distances[u] + weight < distances[v]:
                raise ValueError("The graph contains a negative-weight cycle")

    return distances, predecessors

def shortest_path(target: Vertex[T], predecessors: Dict[Vertex[T], Vertex[T] | None]) -> List[Vertex[T]]:
    
    shortest_path = []
    current_pred = target

    while current_pred is not None:
        shortest_path.append(current_pred)
        current_pred = predecessors[current_pred]
    
    shortest_path.reverse()
    
    return shortest_path
