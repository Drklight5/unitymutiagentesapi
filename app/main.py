from flask import Flask, Response
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
import io

import base64
import mysql.connector
import json

 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>Unity Multiagentes</h1>"



# # Configuración de conexión a MySQL
# db_config = {
#     "host": "localhost",
#     "user": "tu_usuario",
#     "password": "tu_contraseña",
#     "database": "tu_base_de_datos"
# }

# @app.route('/grafica', methods=['GET'])
# def generar_grafica():
#     try:
#         # Conexión a la base de datos
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()

#         # Query para obtener datos
#         query = "SELECT columna_x, columna_y FROM tu_tabla;"
#         cursor.execute(query)
#         datos = cursor.fetchall()

#         # Cerrar conexión
#         cursor.close()
#         conn.close()

#         # Separar datos en listas
#         x = [fila[0] for fila in datos]
#         y = [fila[1] for fila in datos]

#         # Crear la gráfica con Matplotlib
#         plt.figure(figsize=(8, 5))
#         plt.plot(x, y, marker='o', linestyle='-', color='b')
#         plt.title('Gráfica generada desde MySQL')
#         plt.xlabel('Eje X')
#         plt.ylabel('Eje Y')
#         plt.grid(True)

#         # Guardar la imagen en memoria
#         buf = io.BytesIO()
#         plt.savefig(buf, format='png')
#         buf.seek(0)

#         # Convertir la imagen a base64
#         img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
#         buf.close()

#         # Devolver la imagen como respuesta
#         return Response(buf.getvalue(), mimetype='image/png')
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
@app.route('/grafica2', methods=['GET'])
def generar_grafica():
    # Leer los datos desde el archivo JSON
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

    # Formateo de fechas
    date_format = DateFormatter('%Y-%m-%d %H:%M:%S')
    ax1.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    # Ajustes finales
    plt.title(f"Visualización de {data['tractorName']}")
    plt.grid(True)
    plt.tight_layout()

    # Guardar la gráfica en un buffer de memoria
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)  # Cerrar la figura para liberar memoria

    # Devolver la imagen como respuesta HTTP
    return Response(buffer, mimetype='image/png')


# @app.route('/', methods=['GET'])
# def grafica_prueba():

#     # Datos de prueba
#     x = [1, 2, 3, 4, 5]
#     y = [10, 20, 15, 30, 25]

#     # Crear la gráfica
#     plt.figure(figsize=(8, 5))
#     plt.plot(x, y, marker='o', linestyle='-', color='b', label='Datos de prueba')
#     plt.title('Gráfica de Prueba')
#     plt.xlabel('Eje X')
#     plt.ylabel('Eje Y')
#     plt.legend()
#     plt.grid(True)

#     # Guardar la imagen en memoria
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)

#     # Devolver la imagen como respuesta
#     return Response(buf.getvalue(), mimetype='image/png')



@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

# @app.route('/set', methods=['POST'])
# def grafica_prueba():
#     return "Hi"
#     # Datos de prueba
#     x = [1, 2, 3, 4, 5]
#     y = [10, 20, 15, 30, 25]

#     # Crear la gráfica
#     plt.figure(figsize=(8, 5))
#     plt.plot(x, y, marker='o', linestyle='-', color='b', label='Datos de prueba')
#     plt.title('Gráfica de Prueba')
#     plt.xlabel('Eje X')
#     plt.ylabel('Eje Y')
#     plt.legend()
#     plt.grid(True)

#     # Guardar la imagen en memoria
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)

#     # Devolver la imagen como respuesta
#     return Response(buf.getvalue(), mimetype='image/png')
