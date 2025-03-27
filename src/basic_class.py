from typing import TypeVar, Generic, Dict, List, Tuple

T = TypeVar('T')

class Vertex(Generic[T]):

    def __init__(self, name: T) -> None:
        self.name : T = name
    
    def display(self) -> str:
        return f"Vertex({self.name})"


class Graph(Generic[T]):
    
    def __init__(self) -> None:
        self.adjacency: Dict[Vertex[T], List[Tuple[Vertex[T], float]]] = {}    # Adjacency dictionary
    
    def add_edge(self, u: Vertex[T], v: Vertex[T], weight: float) -> None:
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        self.adjacency[u].append((v, weight))


