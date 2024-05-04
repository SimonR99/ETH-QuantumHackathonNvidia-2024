import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

ocean_background = "img/ocean.jpg"

def generate_point_graph_with_weights(n):
    # Create a complete graph with n nodes
    point_graph = nx.Graph()
    positions = {}
    weights = {}

    # Initialize the nodes with positions and random weights
    for node in range(n):
        if node == 0:
            # First node in the center (Port)
            pos = (0.5, 0.5)
        else:
            pos = (np.random.uniform(), np.random.uniform())

        # Save the position for later use
        positions[node] = pos
        # Assign a random weight to each node (if needed)
        weights[node] = np.random.randint(1, 100)
        # Add the node to the graph with position and weight
        point_graph.add_node(node, pos=pos, weight=weights[node])

    # Create edges between every pair of nodes
    for node1 in range(n):
        for node2 in range(node1 + 1, n):
            # Calculate Euclidean distance between nodes as edge weight
            pos1 = positions[node1]
            pos2 = positions[node2]
            distance = np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
            point_graph.add_edge(node1, node2, weight=distance)

    return point_graph

def draw_graph(G, colors, pos):
      img = plt.imread("img/ocean.jpg")
      fig, ax = plt.subplots()
      ax.imshow(img, extent=[-0.1, 1.1, -0.1, 1.1])
      default_axes = plt.axes(frameon=True)
      nx.draw_networkx(G, node_color=colors, node_size=600, alpha=0.8, ax=default_axes, pos=pos)
      edge_labels = nx.get_edge_attributes(G, "weight")
      nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)