import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


red_line = ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"]
blue_line = ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Українських Героїв", "Олімпійська", "Палац 'Україна'", "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки"]
green_line = ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", "Кловська", "Печерська", "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний хутір"]


for line in [red_line, blue_line, green_line]:
    for i in range(len(line) - 1):
        G.add_edge(line[i], line[i+1], weight=2)


interchanges = [
    ("Театральна", "Золоті ворота"),
    ("Хрещатик", "Майдан Незалежності"),
    ("Площа Українських Героїв", "Палац спорту")
]
for u, v in interchanges:
    G.add_edge(u, v, weight=5)


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())
    previous_nodes = {node: None for node in graph.nodes()}

    while unvisited:
        
        current_node = min(unvisited, key=lambda node: distances[node])
        
        if distances[current_node] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_distance = distances[current_node] + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        unvisited.remove(current_node)
    return distances, previous_nodes

def get_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    return path[::-1] if path[0] == end else []


start_st = "Академмістечко"
end_st = "Позняки"
distances, predecessors = dijkstra(G, start_st)
shortest_path = get_path(predecessors, start_st, end_st)


node_colors = []
for node in G.nodes():
    if node in shortest_path: node_colors.append('orange') # Підсвічуємо знайдений шлях
    elif node in red_line: node_colors.append('red')
    elif node in blue_line: node_colors.append('blue')
    elif node in green_line: node_colors.append('green')
    else: node_colors.append('gray')

plt.figure(figsize=(20, 8))
pos = nx.spring_layout(G, seed=42, k=0.15)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=600, font_size=8, font_weight="bold", edge_color="silver")
plt.title(f"Найкоротший шлях за Дейкстрою: {start_st} -> {end_st}", fontsize=15)
plt.show()


print(f"Найкоротший шлях ({distances[end_st]} хв):")
print(" -> ".join(shortest_path))