import networkx as nx
import matplotlib.pyplot as plt

social_media_data = [
    ('user1', 'user2', 'like'),
    ('user1', 'user3', 'comment'),
    ('user2', 'user1', 'share'),
    ('user3', 'user2', 'like'),
    ('user3', 'user1', 'like'),
    ('user4', 'user1', 'comment'),
    ('user4', 'user3', 'share'),
]
G = nx.Graph()
for user1, user2, interaction_type in social_media_data:
    G.add_edge(user1, user2, interaction_type=interaction_type)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, edge_color='gray', font_size=12)
plt.title('Social Media Network', fontsize=14)
plt.axis('off')
plt.show()

degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:")
for user, centrality in degree_centrality.items():
    print(f"{user}: {centrality:.2f}")
