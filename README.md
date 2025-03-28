## Problem Set 1 — Shortest Path Algorithms
This project implements shortest path algorithms, with an application on the Paris Metro network, using Dijkstra and Bellman-Ford.


## Installation
Make sure you have Python 3.10+ installed. Then, clone the repository and install the project in editable mode with:

```bash 
pip install -e .
```

This allows you to make changes in the source code without reinstalling the package.

## Usage
To run the example scenarios using both algorithms:

```bash
python tests/test_shortest_path.py
```

You will see route examples between different stations of Paris such as:

Gare de l'Est → Gare de Lyon

Crimée → Richard Lenoir

Riquet → Abbesses

Each example prints the shortest path and distance.

## Algorithms
Implemented algorithms:

Dijkstra: Fast and optimal for graphs with non-negative weights.

Bellman-Ford: Supports negative weights and detects negative-weight cycles.

Both algorithms return:

---A dictionary of shortest distances from the source
---A dictionary of predecessors to reconstruct paths

## Requirements
No external dependencies are needed.

## Dataset
The file datasets/graph_subway_paris.txt contains:

Vertex identifiers and names

Arc weights representing distances between stations

## Author
This project was developed as part of the first problem set in a Discrete Mathematics course by Louis Bonnecaze (Louis641214).