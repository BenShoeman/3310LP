import networkx as nx

def create_graph():
  # Node 0 is Fleming, Node 49 is Duane
  G = nx.DiGraph()

  G.add_edge(0, 1, weight=150.)

  G.add_edge(1, 2, weight=200.)
  G.add_edge(1, 3, weight=133.)

  G.add_edge(2, 4, weight=100.)

  G.add_edge(3, 5, weight=200.)

  G.add_edge(4, 6, weight=200.)
  G.add_edge(4, 7, weight=700.)

  G.add_edge(5, 8, weight=67.)
  G.add_edge(5, 9, weight=133.)

  G.add_edge(6, 8, weight=100.)

  G.add_edge(7, 10, weight=167.)

  G.add_edge(8, 9, weight=150.)

  G.add_edge(9, 11, weight=100.)

  G.add_edge(10, 11, weight=700.)
  G.add_edge(10, 12, weight=400.)

  G.add_edge(11, 15, weight=250.)

  G.add_edge(12, 13, weight=300.)
  G.add_edge(12, 16, weight=267.)

  G.add_edge(13, 14, weight=267.)
  G.add_edge(13, 17, weight=267.)

  G.add_edge(14, 15, weight=400.)
  G.add_edge(14, 19, weight=267.)

  G.add_edge(15, 22, weight=250.)
  G.add_edge(15, 36, weight=700.)

  G.add_edge(16, 17, weight=267.)
  G.add_edge(16, 27, weight=300.)

  G.add_edge(17, 18, weight=100.)

  G.add_edge(18, 19, weight=167.)
  G.add_edge(18, 23, weight=100.)

  G.add_edge(19, 20, weight=100.)
  G.add_edge(19, 23, weight=167.)

  G.add_edge(20, 21, weight=50.)
  G.add_edge(20, 24, weight=167.)

  G.add_edge(21, 22, weight=100.)
  G.add_edge(21, 25, weight=200.)

  G.add_edge(22, 26, weight=200.)

  G.add_edge(23, 29, weight=200.)

  G.add_edge(24, 25, weight=50.)
  G.add_edge(24, 30, weight=200.)
  G.add_edge(24, 31, weight=200.)

  G.add_edge(25, 26, weight=67.)
  G.add_edge(25, 32, weight=200.)

  G.add_edge(26, 34, weight=133.)

  G.add_edge(27, 28, weight=300.)
  G.add_edge(27, 40, weight=300.)

  G.add_edge(28, 29, weight=150.)
  G.add_edge(28, 41, weight=300.)

  G.add_edge(29, 30, weight=150.)

  G.add_edge(30, 31, weight=100.)
  G.add_edge(30, 42, weight=300.)

  G.add_edge(31, 32, weight=50.)
  G.add_edge(31, 37, weight=67.)
  G.add_edge(31, 38, weight=100.)

  G.add_edge(32, 33, weight=50.)

  G.add_edge(33, 34, weight=133.)
  G.add_edge(33, 37, weight=67.)
  G.add_edge(33, 39, weight=100.)

  G.add_edge(34, 35, weight=100.)
  G.add_edge(34, 44, weight=333.)

  G.add_edge(35, 36, weight=33.)
  G.add_edge(35, 44, weight=233.)

  G.add_edge(36, 45, weight=200.)

  G.add_edge(37, 38, weight=67.)
  G.add_edge(37, 39, weight=67.)

  G.add_edge(38, 39, weight=100.)
  G.add_edge(38, 42, weight=150.)

  G.add_edge(39, 44, weight=150.)

  G.add_edge(40, 46, weight=167.)
  G.add_edge(40, 41, weight=300.)

  G.add_edge(41, 42, weight=267.)
  G.add_edge(41, 47, weight=167.)

  G.add_edge(42, 43, weight=100.)

  G.add_edge(43, 44, weight=200.)
  G.add_edge(43, 48, weight=250.)

  G.add_edge(44, 45, weight=100.)

  G.add_edge(46, 47, weight=300.)

  G.add_edge(47, 48, weight=167.)
  G.add_edge(47, 49, weight=67.)

  # Shortest path algorithm for simplex method requires directed graph, but we
  # have undirected graph so we'll add backedge for every edge to make it
  # directed
  for e in G.edges():
    u,v = e
    G.add_edge(v, u, weight=G[u][v]['weight'])
  
  return G
