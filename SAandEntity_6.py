import networkx as nx
import matplotlib.pyplot as plt

# Simplified Instagram data with 4 users
instagram_data = [
    ('user1', 'user2', 'follow'),
    ('user1', 'user3', 'follow'),
    ('user2', 'user1', 'mention'),
    ('user3', 'user1', 'reply'),
    ('user4', 'user1', 'follow')
]

# Create directed graph and add edges
G = nx.DiGraph()
for u1, u2, interaction in instagram_data:
    G.add_edge(u1, u2, interaction_type=interaction)

# Calculate degree centrality and print top 2 users
degree_centrality = nx.degree_centrality(G)
top_users = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:2]
for user, centrality in top_users:
    print(f"{user}: Degree Centrality = {centrality:.2f}")

# Plot the network
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw_networkx(G, pos, node_color='lightblue', node_size=1500, font_size=12, font_family='sans-serif', edge_color='gray', width=2, arrows=True)
edge_labels = {(u1, u2): interaction for u1, u2, interaction in instagram_data}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title('Instagram Interaction Network')
plt.axis('off')
plt.show()
