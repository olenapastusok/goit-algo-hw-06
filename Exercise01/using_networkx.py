import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


# Червона лінія (М1)
red_line = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", 
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", 
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", 
    "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]

# Синя лінія (М2)
blue_line = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", 
    "Контрактова площа", "Поштова площа", "Майдан Незалежності", 
    "Площа Українських Героїв", "Олімпійська", "Палац 'Україна'", 
    "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки"
]

# Зелена лінія (М3)
green_line = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", 
    "Палац спорту", "Кловська", "Печерська", "Дружби народів", 
    "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний хутір"
]

for line in [red_line, blue_line, green_line]:
    for i in range(len(line) - 1):
        G.add_edge(line[i], line[i+1])

# Пересадочні вузли (Interchanges)
interchanges = [
    ("Театральна", "Золоті ворота"),           # Червона <-> Зелена
    ("Хрещатик", "Майдан Незалежності"),      # Червона <-> Синя
    ("Площа Українських Героїв", "Палац спорту") # Синя <-> Зелена
]
G.add_edges_from(interchanges)


node_colors = []
for node in G.nodes():
    if node in red_line:
        node_colors.append('red')
    elif node in blue_line:
        node_colors.append('blue')
    elif node in green_line:
        node_colors.append('green')
    else:
        node_colors.append('gray')


plt.figure(figsize=(20, 7))
pos = nx.spring_layout(G, seed=42, k=0.15) # k регулює відстань між вузлами

nx.draw(G, pos, 
        with_labels=True, 
        node_color=node_colors, 
        node_size=600, 
        font_size=8, 
        font_weight="bold",
        edge_color="silver",
        alpha=0.8)

plt.title("Модель Київського Метрополітену", fontsize=15)
plt.show()

print(f"Кількість станцій: {G.number_of_nodes()}")
print(f"Кількість сполучень: {G.number_of_edges()}")

# Пошук пересадочних хабів (ступінь вершини > 2)
print("\nПересадочні станції та вузли:")
degrees = dict(G.degree())
hubs = {node: deg for node, deg in degrees.items() if deg > 2}
for node, deg in sorted(hubs.items(), key=lambda x: x[1], reverse=True):
    print(f" - {node}: {deg} зв'язки")