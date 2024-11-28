import json
import matplotlib.pyplot as plt
from datetime import datetime

# Cargar el JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Extraer los datos
timestamps = [datetime.fromisoformat(point["timestamp"]) for point in data["points"]]
positions_x = [point["position"]["x"] for point in data["points"]]
positions_y = [point["position"]["y"] for point in data["points"]]
positions_z = [point["position"]["z"] for point in data["points"]]
speeds = [point["speed"] for point in data["points"]]

# Crear la figura y los ejes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Gráfica de posiciones
ax1.plot(timestamps, positions_x, label='Posición X', color='blue')
ax1.plot(timestamps, positions_y, label='Posición Y', color='green')
ax1.plot(timestamps, positions_z, label='Posición Z', color='red')
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Posición', color='black')
ax1.tick_params(axis='y')
ax1.legend(loc='upper left')

# Eje secundario para velocidad
ax2 = ax1.twinx()
ax2.plot(timestamps, speeds, label='Velocidad', color='orange', linestyle='dashed')
ax2.set_ylabel('Velocidad', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.legend(loc='upper right')

# Ajustes finales
plt.title(f"Visualización de {data['tractorName']}")
plt.grid(True)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
