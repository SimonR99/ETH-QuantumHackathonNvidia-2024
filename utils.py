import networkx as nx
import numpy as np

def generate_point_graph_with_weights(n):
      # Create a complete graph with n nodes
      point_graph = nx.Graph()
      first_iteration = True
      for node in range(n):
            positions = (np.random.uniform(), np.random.uniform())
            if first_iteration:
                  positions = (0.5,0.5) # First node in the center (Port)
                  first_iteration = False
            point_graph.add_node(node, pos=positions,weight=np.random.randint(1, 100))
      return point_graph