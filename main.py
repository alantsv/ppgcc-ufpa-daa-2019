#!/usr/bin/env python3

__author__ = "Alan Veloso (alantsv@gmail.com)"

import networkx as nx
import matplotlib.pyplot as plt
from eulerian_graph import fleury

def main():
    # Non-oriented graph
    graph = {"A": ["B", "C", "D", "E"],
             "B": ["A", "C"],
             "C": ["A", "B", "D"],
             "D": ["A", "C", "E"],
             "E": ["A", "D"]}

    G = nx.Graph()
    nodes_graph = list(graph.keys())
    G.add_nodes_from(nodes_graph)
    print("Nodes of graph: ")
    print(G.nodes())
    
    # Eulerian path using Fleury's algorithm on non-oriented graph
    eulerian_cycle = fleury(graph)
    print('1st Eulerian Cycle')
    print(eulerian_cycle)
    G.add_edges_from(eulerian_cycle)

    nx.draw(G, with_labels = True, node_color = 'r')
    plt.show() # display

if __name__ == "__main__":
    main()