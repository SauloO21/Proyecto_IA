# Proyecto_IA
Proyecto de la materia Inteligencia Artificial de 6to Semestre grupo A de ISC
import heapq
import matplotlib.pyplot as plt


grafo = {
    'A': {'B': 180, 'C': 146, 'N': 200, 'AA': 160},  # Punto inicial
    'B': {'A': 180, 'D': 304, 'O': 120},
    'C': {'A': 146, 'D': 80, 'L': 135, 'J': 60, 'P': 150},
    'D': {'B': 304, 'C': 80, 'E': 30, 'Q': 90},
    'E': {'D': 30, 'F': 30, 'R': 110},
    'F': {'E': 30, 'G': 40, 'S': 80},
    'G': {'F': 40, 'H': 60, 'T': 70},
    'H': {'G': 60, 'I': 10, 'U': 130},
    'I': {'H': 10, 'J': 50, 'K': 60, 'V': 140},
    'J': {'I': 50, 'C': 60, 'K': 45, 'W': 100},
    'K': {'J': 45, 'I': 60, 'M': 135, 'X': 90},
    'L': {'C': 135, 'M': 171, 'Y': 160},
    'M': {'K': 135, 'L': 171, 'N': 80, 'Z': 120},
    'N': {'A': 200, 'M': 80, 'O': 110, 'AA': 145},
    'O': {'B': 120, 'N': 110, 'P': 95},
    'P': {'C': 150, 'O': 95, 'Q': 130},
    'Q': {'D': 90, 'P': 130, 'R': 85},
    'R': {'E': 110, 'Q': 85, 'S': 75},
    'S': {'F': 80, 'R': 75, 'T': 65},
    'T': {'G': 70, 'S': 65, 'U': 115},
    'U': {'H': 130, 'T': 115, 'V': 100},
    'V': {'I': 140, 'U': 100, 'W': 90},
    'W': {'J': 100, 'V': 90, 'X': 85},
    'X': {'K': 90, 'W': 85, 'Y': 105},
    'Y': {'L': 160, 'X': 105, 'Z': 95},
    'Z': {'M': 120, 'Y': 95},
    'AA': {'A': 160, 'N': 145, 'BB': 130},
    'BB': {'AA': 130, 'CC': 90, 'O': 110},
    'CC': {'BB': 90, 'DD': 100, 'C': 170},
    'DD': {'CC': 100, 'EE': 85, 'D': 100},
    'EE': {'DD': 85, 'E': 120, 'FF': 95},
    'FF': {'EE': 95, 'F': 90}
}


posiciones = {
    'A': (0, 8),    
    'B': (-2, 6),
    'C': (1, 5),
    'D': (-3, 4),
    'E': (-4, 2),
    'F': (-2, 0),
    'G': (-1, -2),
    'H': (-2, -4),
    'I': (1, -5),
    'J': (1.5, 2),
    'K': (3.5, -1),
    'L': (4, 3),
    'M': (6, -2),
    'N': (2, 7),
    'O': (0, 6),
    'P': (2, 4),
    'Q': (-1, 3),
    'R': (-3, 1),
    'S': (-1, -1),
    'T': (0, -3),
    'U': (-1, -5),
    'V': (2, -4),
    'W': (3, 1),
    'X': (4, -1),
    'Y': (5, 2),
    'Z': (6, 0),
    'AA': (-1, 10),
    'BB': (-3, 8),
    'CC': (0, 7),
    'DD': (-5, 5),
    'EE': (-6, 3),
    'FF': (-4, 1)
}


hospitales = {
    "Hospital ABC": 'I',
    "Hospital IMSS": 'N',
    "Hospital Benito": 'M',
    "Hospital IA": 'U',
    "Hospital UAC": 'E',
    "Hospital General": 'AA',
    "Hospital Sur": 'Z'
}


def dijkstra_ruta(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    cola = [(0, origen, [origen])]  # (distancia, nodo, ruta)
    ruta_final = {nodo: [] for nodo in grafo}

    while cola:
        distancia_actual, nodo_actual, ruta_actual = heapq.heappop(cola)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                ruta_final[vecino] = ruta_actual + [vecino]
                heapq.heappush(cola, (distancia, vecino, ruta_final[vecino]))
    
    return distancias, ruta_final

print("\nPosiciones disponibles para la ambulancia:")
for nodo in grafo.keys():
    print(f"- {nodo}")
origen = input("Ingrese el nodo donde está la ambulancia: ")
if origen not in grafo:
    print("Nodo no válido. Usando 'A' por defecto.")
    origen = 'A'

print("\nHospitales disponibles:")
for nombre in hospitales.keys():
    print(f"- {nombre}")
hospital_elegido = input("Ingrese el nombre del hospital al que desea ir: ")
if hospital_elegido not in hospitales:
    print("Hospital no válido. Seleccionando 'Hospital ABC' por defecto.")
    hospital_elegido = "Hospital ABC"
destino = hospitales[hospital_elegido]

# Calcular ruta y distancia
distancias, ruta = dijkstra_ruta(grafo, origen)
ruta_completa = ruta[destino]
distancia_total = distancias[destino]

# Dibujar el mapa
plt.figure(figsize=(12, 10))
plt.title(f"Ruta más corta desde {origen} a {hospital_elegido}")

# Dibujar nodos
for nodo, (x, y) in posiciones.items():
    if nodo not in hospitales.values():  # Si no es un hospital, dibujar con letra
        plt.scatter(x, y, c='lightblue', s=100)
        plt.text(x, y, nodo, fontsize=10, ha='center', va='center')

# Dibujar aristas
for nodo, vecinos in grafo.items():
    x1, y1 = posiciones[nodo]
    for vecino, peso in vecinos.items():
        x2, y2 = posiciones[vecino]
        plt.plot([x1, x2], [y1, y2], 'k-', lw=1)
        plt.text((x1 + x2) / 2, (y1 + y2) / 2, str(peso), fontsize=8, color='gray')

# Dibujar ambulancia
x_a, y_a = posiciones[origen]
plt.scatter(x_a, y_a, c='red', s=150, label="Ambulancia", marker='*')
if origen not in hospitales.values():
    plt.text(x_a, y_a, origen, fontsize=10, ha='center', va='center')

# Dibujar hospitales con sus nombres
for nombre, nodo in hospitales.items():
    x, y = posiciones[nodo]
    color = 'green' if nombre == hospital_elegido else 'blue'
    plt.scatter(x, y, c=color, s=100, marker='^', label=nombre if color == 'blue' else f"{nombre} (destino)")
    plt.text(x, y, nombre, fontsize=8, ha='center', va='center', color='white', weight='bold')

# Dibujar ruta
if ruta_completa:
    x_ruta = [posiciones[nodo][0] for nodo in ruta_completa]
    y_ruta = [posiciones[nodo][1] for nodo in ruta_completa]
    plt.plot(x_ruta, y_ruta, 'g--', lw=2, label="Ruta más corta")

# Configurar el mapa sin marco de coordenadas y mover el cuadro de distancia
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.text(6, -5, f"Distancia: {distancia_total} m", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))  # Movido a esquina inferior derecha
plt.grid(True)
plt.axis('equal')
plt.axis('off')
plt.show()


print(f"\nDistancia más corta desde {origen} a {hospital_elegido}: {distancia_total} metros")
print(f"Ruta más corta: {' -> '.join(ruta_completa)}")
