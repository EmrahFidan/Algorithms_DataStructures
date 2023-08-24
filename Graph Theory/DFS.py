""" 

A  --  B   --  C
       |       |
       D   --  E
       
"""

# Graf yapısını temsil eden sözlük
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

# DFS algoritması
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')  # Düğümü ziyaret et ve yazdır
        visited.add(node)      # Düğümü ziyaret edildi olarak işaretle
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)  # Komşuları için DFS'i rekürsif olarak çağır

# DFS'yi başlatmak için kullanılacak başlangıç düğümü
start_node = 'A'

# Ziyaret edilen düğümleri takip etmek için küme
visited_nodes = set()

# DFS'yi başlat
dfs(graph, start_node, visited_nodes)
