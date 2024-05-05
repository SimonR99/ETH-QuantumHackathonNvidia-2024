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

def draw_graph(graph):
    img = plt.imread("img/ocean.jpg")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[-0.1, 1.1, -0.1, 1.1])
    
    positions = nx.get_node_attributes(graph, 'pos')
    edge_labels = nx.get_edge_attributes(graph, "weight")
    
    labels_position = {node: (position[0], position[1] + 0.06) for node, position in positions.items()}
    labels = {node: graph.nodes[node]['weight'] for node in graph.nodes()}
    
    node_colors = ['yellow' if node == 0 else 'lightblue' for node in graph.nodes()]

      
    # Drawing the graph
    nx.draw_networkx_labels(graph, labels_position, labels=labels, font_size=12, font_color='black')
    # nx.draw_networkx_edge_labels(graph, pos=positions, edge_labels=edge_labels)
    nx.draw(graph, positions, with_labels=True, node_color=node_colors, edge_color='black', node_size=250)

    # Show the graph
    plt.title('Ocean waste simulation')
    plt.show()
    
    
def draw_partitionned_graph(graphs, colors):
    img = plt.imread("img/ocean.jpg")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[-0.1, 1.1, -0.1, 1.1])
    
    for i in range(len(graphs)):
        graph = graphs[i]
        color = colors[i]        
    
        positions = nx.get_node_attributes(graph, 'pos')
        edge_labels = nx.get_edge_attributes(graph, "weight")
        
        labels_position = {node: (position[0], position[1] + 0.06) for node, position in positions.items()}
        labels = {node: graph.nodes[node]['weight'] for node in graph.nodes()}
        nx.draw(graph, positions, with_labels=True, node_color=color, edge_color='black', node_size=250)

    # Show the graph
    plt.title('Ocean waste simulation')
    plt.show()