import networkx as nx

def create_graph():
  # Node 0 is Fleming, Node 49 is Duane
  G = nx.DiGraph()

  G.add_edge(0, 1, distance=150)

  G.add_edge(1, 2, distance=200)
  G.add_edge(1, 3, distance=133)

  G.add_edge(2, 4, distance=100)

  G.add_edge(3, 5, distance=200)

  G.add_edge(4, 6, distance=200)
  G.add_edge(4, 7, distance=700)

  G.add_edge(5, 8, distance=67)
  G.add_edge(5, 9, distance=133)

  G.add_edge(6, 8, distance=100)

  G.add_edge(7, 10, distance=167)

  G.add_edge(8, 9, distance=150)

  G.add_edge(9, 11, distance=100)

  G.add_edge(10, 11, distance=700)
  G.add_edge(10, 12, distance=400)

  G.add_edge(11, 15, distance=250)

  G.add_edge(12, 13, distance=300)
  G.add_edge(12, 16, distance=267)

  G.add_edge(13, 14, distance=267)
  G.add_edge(13, 17, distance=267)

  G.add_edge(14, 15, distance=400)
  G.add_edge(14, 19, distance=267)

  G.add_edge(15, 22, distance=250)
  G.add_edge(15, 36, distance=700)

  G.add_edge(16, 17, distance=267)
  G.add_edge(16, 27, distance=300)

  G.add_edge(17, 18, distance=100)

  G.add_edge(18, 19, distance=167)
  G.add_edge(18, 23, distance=100)

  G.add_edge(19, 20, distance=100)
  G.add_edge(19, 23, distance=167)

  G.add_edge(20, 21, distance=50)
  G.add_edge(20, 24, distance=167)

  G.add_edge(21, 22, distance=100)
  G.add_edge(21, 25, distance=200)

  G.add_edge(22, 26, distance=200)

  G.add_edge(23, 29, distance=200)

  G.add_edge(24, 25, distance=50)
  G.add_edge(24, 30, distance=200)
  G.add_edge(24, 31, distance=200)

  G.add_edge(25, 26, distance=67)
  G.add_edge(25, 32, distance=200)

  G.add_edge(26, 34, distance=133)

  G.add_edge(27, 28, distance=300)
  G.add_edge(27, 40, distance=300)

  G.add_edge(28, 29, distance=150)
  G.add_edge(28, 41, distance=300)

  G.add_edge(29, 30, distance=150)

  G.add_edge(30, 31, distance=100)
  G.add_edge(30, 42, distance=300)

  G.add_edge(31, 32, distance=50)
  G.add_edge(31, 37, distance=67)
  G.add_edge(31, 38, distance=100)

  G.add_edge(32, 33, distance=50)

  G.add_edge(33, 34, distance=133)
  G.add_edge(33, 37, distance=67)
  G.add_edge(33, 39, distance=100)

  G.add_edge(34, 35, distance=100)
  G.add_edge(34, 44, distance=333)

  G.add_edge(35, 36, distance=33)
  G.add_edge(35, 44, distance=233)

  G.add_edge(36, 45, distance=200)

  G.add_edge(37, 38, distance=67)
  G.add_edge(37, 39, distance=67)

  G.add_edge(38, 39, distance=100)
  G.add_edge(38, 42, distance=150)

  G.add_edge(39, 44, distance=150)

  G.add_edge(40, 46, distance=167)
  G.add_edge(40, 41, distance=300)

  G.add_edge(41, 42, distance=267)
  G.add_edge(41, 47, distance=167)

  G.add_edge(42, 43, distance=100)

  G.add_edge(43, 44, distance=200)
  G.add_edge(43, 48, distance=250)

  G.add_edge(44, 45, distance=100)

  G.add_edge(46, 47, distance=300)

  G.add_edge(47, 48, distance=167)
  G.add_edge(47, 49, distance=67)

  # Shortest path algorithm for simplex method requires directed graph, but we
  # have undirected graph so we'll add backedge for every edge to make it
  # directed
  for e in G.edges():
    u,v = e
    G.add_edge(v, u, distance=G[u][v]['distance'])
  
  return G
