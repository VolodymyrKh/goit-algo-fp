import heapq

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "Z", weight=6)
G.add_edge("E", "Z", weight=3)

# Implementation of Dijkstra's algorithm
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    previous_nodes = {vertex: None for vertex in graph}
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if a better path is found
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # If a shorter path to a neighbor is found
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths, previous_nodes

def reconstruct_path(previous_nodes, start, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else []

shortest_paths, previous_nodes = dijkstra(G, "A")

print("Shortest distances from A:")
for node, dist in shortest_paths.items():
    print(f"{node}: {dist}, шлях: {reconstruct_path(previous_nodes, 'A', node)}")

print(shortest_paths)

# Graph visualization
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()