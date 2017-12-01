import networkx as nx
import numpy as np
import simplex

def shortest_path(G, source, target):
# Find shortest path in graph G using the Simplex Method.
# Assume all nodes in G are labeled 0,1,2,...,n-1 where n is number of nodes
    # Create tableau for LP formulation
    n = len(G) # len(G) is number of nodes
    b = np.array(np.zeros((1, n)))[0]
    b[source] = 1; b[target] = -1
    A = np.zeros((n, n*n))
    c = np.array(np.zeros((1, n*n)))[0]
    for v in G.nodes():
        for u in G.predecessors(v):
            A[v][u*n + v] = -1
        for u in G.successors(v):
            A[v][v*n + u] = 1
            c[v*n + u] = G[v][u]['weight']

    # Now solve dual-simplex problem for shortest path
    t = simplex.Tableau(n*n,n)
    t.b = c
    t.a = A.T
    t.c = -b
    t.simplex()
    solution = t.getY()

    # Finally, extract path from solution
    path = []
    soln_indices = np.where(solution == 1)[0]
    for i in soln_indices:
        u = i // n
        v = i % n
        path.append((u,v))
    
    return path
