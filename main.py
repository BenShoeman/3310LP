import networkx as nx
from shortestpath import *

def simple_example():
    G = nx.DiGraph()
    G.add_edge(0, 1, weight=2.)
    G.add_edge(0, 2, weight=6.)
    G.add_edge(0, 3, weight=5.)
    G.add_edge(1, 3, weight=4.)
    G.add_edge(2, 3, weight=1.)
    p = shortest_path(G, 0, 3)
    print(p)

def main():
    simple_example()

if __name__ == '__main__':
    main()