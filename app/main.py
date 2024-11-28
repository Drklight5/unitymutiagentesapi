from flask import Flask, Response
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
from datetime import datetime

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
@app.route('/graficar.png', methods=['GET'])
def generar_grafica():
    # Leer los datos desde el archivo JSON
    with open('data.json', 'r') as file:
        data = json.load(file)

    data = {
    "tractorName": "TractorDefinitivo",
    "points": [
        {
            "timestamp": "2024-11-27T13:26:17.4475571-06:00",
            "position": {
                "x": 63.338768005371097,
                "y": 0.0,
                "z": 48.68126678466797
            },
            "speed": 0.0
        },
        {
            "timestamp": "2024-11-27T13:26:19.2215201-06:00",
            "position": {
                "x": 60.5943603515625,
                "y": 4.76837158203125e-7,
                "z": 51.73492431640625
            },
            "speed": 7.530264377593994
        },
        {
            "timestamp": "2024-11-27T13:26:20.2223651-06:00",
            "position": {
                "x": 53.95814895629883,
                "y": 4.76837158203125e-7,
                "z": 52.75865936279297
            },
            "speed": 7.855837821960449
        },
        {
            "timestamp": "2024-11-27T13:26:21.2220697-06:00",
            "position": {
                "x": 46.6319465637207,
                "y": 4.76837158203125e-7,
                "z": 49.55059814453125
            },
            "speed": 7.989655017852783
        },
        {
            "timestamp": "2024-11-27T13:26:22.2251882-06:00",
            "position": {
                "x": 39.402740478515628,
                "y": 4.76837158203125e-7,
                "z": 46.184326171875
            },
            "speed": 7.538568496704102
        },
        {
            "timestamp": "2024-11-27T13:26:23.2230360-06:00",
            "position": {
                "x": 35.77399444580078,
                "y": 4.76837158203125e-7,
                "z": 43.84705352783203
            },
            "speed": 1.3345067501068116
        },
        {
            "timestamp": "2024-11-27T13:26:24.2241104-06:00",
            "position": {
                "x": 38.803802490234378,
                "y": 4.76837158203125e-7,
                "z": 43.61322021484375
            },
            "speed": 3.7762954235076906
        },
        {
            "timestamp": "2024-11-27T13:26:25.2242634-06:00",
            "position": {
                "x": 41.62853240966797,
                "y": 4.76837158203125e-7,
                "z": 43.872703552246097
            },
            "speed": 2.217439651489258
        },
        {
            "timestamp": "2024-11-27T13:26:26.2240184-06:00",
            "position": {
                "x": 44.133628845214847,
                "y": 4.76837158203125e-7,
                "z": 43.90666961669922
            },
            "speed": 2.578930139541626
        },
        {
            "timestamp": "2024-11-27T13:26:27.2249799-06:00",
            "position": {
                "x": 46.59200668334961,
                "y": 4.76837158203125e-7,
                "z": 43.91132354736328
            },
            "speed": 2.3020331859588625
        },
        {
            "timestamp": "2024-11-27T13:26:28.2260244-06:00",
            "position": {
                "x": 49.128849029541019,
                "y": 4.76837158203125e-7,
                "z": 43.91162109375
            },
            "speed": 2.549816846847534
        },
        {
            "timestamp": "2024-11-27T13:26:29.2288308-06:00",
            "position": {
                "x": 50.490177154541019,
                "y": 4.76837158203125e-7,
                "z": 41.961692810058597
            },
            "speed": 2.5099868774414064
        },
        {
            "timestamp": "2024-11-27T13:26:30.2318837-06:00",
            "position": {
                "x": 48.08831787109375,
                "y": 4.76837158203125e-7,
                "z": 40.91960144042969
            },
            "speed": 2.9405856132507326
        },
        {
            "timestamp": "2024-11-27T13:26:31.2328080-06:00",
            "position": {
                "x": 45.47811508178711,
                "y": 4.76837158203125e-7,
                "z": 40.91302490234375
            },
            "speed": 2.783046007156372
        },
        {
            "timestamp": "2024-11-27T13:26:32.2338792-06:00",
            "position": {
                "x": 42.827178955078128,
                "y": 4.76837158203125e-7,
                "z": 40.912437438964847
            },
            "speed": 2.456979990005493
        },
        {
            "timestamp": "2024-11-27T13:26:33.2342943-06:00",
            "position": {
                "x": 40.19656753540039,
                "y": 4.76837158203125e-7,
                "z": 40.91242218017578
            },
            "speed": 2.7776594161987306
        },
        {
            "timestamp": "2024-11-27T13:26:34.2360546-06:00",
            "position": {
                "x": 37.58577346801758,
                "y": 4.76837158203125e-7,
                "z": 40.912376403808597
            },
            "speed": 2.5120110511779787
        },
        {
            "timestamp": "2024-11-27T13:26:35.2398312-06:00",
            "position": {
                "x": 35.69586181640625,
                "y": 4.76837158203125e-7,
                "z": 39.41851043701172
            },
            "speed": 3.180574655532837
        },
        {
            "timestamp": "2024-11-27T13:26:36.2408712-06:00",
            "position": {
                "x": 38.3455696105957,
                "y": 4.76837158203125e-7,
                "z": 38.131919860839847
            },
            "speed": 2.656902551651001
        },
        {
            "timestamp": "2024-11-27T13:26:37.2408041-06:00",
            "position": {
                "x": 41.00034713745117,
                "y": 4.76837158203125e-7,
                "z": 37.94197082519531
            },
            "speed": 2.684623956680298
        },
        {
            "timestamp": "2024-11-27T13:26:38.2424738-06:00",
            "position": {
                "x": 43.49553298950195,
                "y": 4.76837158203125e-7,
                "z": 37.916175842285159
            },
            "speed": 2.2045583724975588
        },
        {
            "timestamp": "2024-11-27T13:26:39.2441993-06:00",
            "position": {
                "x": 46.01718521118164,
                "y": 4.76837158203125e-7,
                "z": 37.91236114501953
            },
            "speed": 2.6522774696350099
        },
        {
            "timestamp": "2024-11-27T13:26:40.2448905-06:00",
            "position": {
                "x": 48.505836486816409,
                "y": 4.76837158203125e-7,
                "z": 37.91236114501953
            },
            "speed": 2.2009220123291017
        },
        {
            "timestamp": "2024-11-27T13:26:41.2462661-06:00",
            "position": {
                "x": 50.43965148925781,
                "y": 4.76837158203125e-7,
                "z": 36.65071105957031
            },
            "speed": 3.2185659408569338
        },
        {
            "timestamp": "2024-11-27T13:26:42.2497502-06:00",
            "position": {
                "x": 48.878868103027347,
                "y": 4.76837158203125e-7,
                "z": 34.92413330078125
            },
            "speed": 3.166067361831665
        },
        {
            "timestamp": "2024-11-27T13:26:43.2492001-06:00",
            "position": {
                "x": 46.099639892578128,
                "y": 4.76837158203125e-7,
                "z": 34.91361999511719
            },
            "speed": 2.7295877933502199
        },
        {
            "timestamp": "2024-11-27T13:26:44.2527299-06:00",
            "position": {
                "x": 43.48849868774414,
                "y": 4.76837158203125e-7,
                "z": 34.91242218017578
            },
            "speed": 2.7983336448669435
        },
        {
            "timestamp": "2024-11-27T13:26:45.2532672-06:00",
            "position": {
                "x": 40.830596923828128,
                "y": 4.76837158203125e-7,
                "z": 34.91239929199219
            },
            "speed": 2.477395534515381
        },
        {
            "timestamp": "2024-11-27T13:26:46.2533969-06:00",
            "position": {
                "x": 38.19416046142578,
                "y": 4.76837158203125e-7,
                "z": 34.912384033203128
            },
            "speed": 2.8030874729156496
        },
        {
            "timestamp": "2024-11-27T13:26:47.2553004-06:00",
            "position": {
                "x": 35.75553512573242,
                "y": 4.76837158203125e-7,
                "z": 34.2640380859375
            },
            "speed": 3.7542128562927248
        },
        {
            "timestamp": "2024-11-27T13:26:48.2559671-06:00",
            "position": {
                "x": 37.6146240234375,
                "y": 4.76837158203125e-7,
                "z": 32.26836395263672
            },
            "speed": 3.3708958625793459
        },
        {
            "timestamp": "2024-11-27T13:26:49.2589071-06:00",
            "position": {
                "x": 40.37611770629883,
                "y": 4.76837158203125e-7,
                "z": 31.96286964416504
            },
            "speed": 2.3593175411224367
        },
        {
            "timestamp": "2024-11-27T13:26:50.2604071-06:00",
            "position": {
                "x": 42.89252471923828,
                "y": 4.76837158203125e-7,
                "z": 31.91900062561035
            },
            "speed": 2.769073247909546
        },
        {
            "timestamp": "2024-11-27T13:26:51.2601911-06:00",
            "position": {
                "x": 45.40072250366211,
                "y": 4.76837158203125e-7,
                "z": 31.91312599182129
            },
            "speed": 2.298138380050659
        },
        {
            "timestamp": "2024-11-27T13:26:52.2607731-06:00",
            "position": {
                "x": 47.90005874633789,
                "y": 4.76837158203125e-7,
                "z": 31.912599563598634
            },
            "speed": 2.75244140625
        },
        {
            "timestamp": "2024-11-27T13:26:53.2616956-06:00",
            "position": {
                "x": 50.25975799560547,
                "y": 4.76837158203125e-7,
                "z": 31.45780372619629
            },
            "speed": 3.3343400955200197
        },
        {
            "timestamp": "2024-11-27T13:26:54.2626051-06:00",
            "position": {
                "x": 49.667903900146487,
                "y": 4.76837158203125e-7,
                "z": 28.928743362426759
            },
            "speed": 3.505983829498291
        },
        {
            "timestamp": "2024-11-27T13:26:55.2635363-06:00",
            "position": {
                "x": 46.754249572753909,
                "y": 4.76837158203125e-7,
                "z": 28.914514541625978
            },
            "speed": 2.3412187099456789
        },
        {
            "timestamp": "2024-11-27T13:26:56.2640328-06:00",
            "position": {
                "x": 44.118553161621097,
                "y": 4.76837158203125e-7,
                "z": 28.91265296936035
            },
            "speed": 2.7165045738220217
        },
        {
            "timestamp": "2024-11-27T13:26:57.2658306-06:00",
            "position": {
                "x": 41.49911117553711,
                "y": 4.76837158203125e-7,
                "z": 28.91258430480957
            },
            "speed": 2.7618958950042726
        },
        {
            "timestamp": "2024-11-27T13:26:58.2658870-06:00",
            "position": {
                "x": 38.84367752075195,
                "y": 4.76837158203125e-7,
                "z": 28.912538528442384
            },
            "speed": 2.466265916824341
        },
        {
            "timestamp": "2024-11-27T13:26:59.2695816-06:00",
            "position": {
                "x": 36.31699752807617,
                "y": 4.76837158203125e-7,
                "z": 28.91251564025879
            },
            "speed": 1.8998780250549317
        },
        {
            "timestamp": "2024-11-27T13:27:00.2716523-06:00",
            "position": {
                "x": 35.15886688232422,
                "y": 4.76837158203125e-7,
                "z": 32.85749816894531
            },
            "speed": 7.84748649597168
        },
        {
            "timestamp": "2024-11-27T13:27:01.2732921-06:00",
            "position": {
                "x": 34.85352325439453,
                "y": 4.76837158203125e-7,
                "z": 40.85132598876953
            },
            "speed": 7.998191833496094
        },
        {
            "timestamp": "2024-11-27T13:27:02.2732761-06:00",
            "position": {
                "x": 34.548484802246097,
                "y": 4.76837158203125e-7,
                "z": 48.84577941894531
            },
            "speed": 7.999284267425537
        },
        {
            "timestamp": "2024-11-27T13:27:03.2736906-06:00",
            "position": {
                "x": 34.2363395690918,
                "y": 4.76837158203125e-7,
                "z": 56.832679748535159
            },
            "speed": 7.962594032287598
        },
        {
            "timestamp": "2024-11-27T13:27:04.2757278-06:00",
            "position": {
                "x": 33.81614303588867,
                "y": 4.76837158203125e-7,
                "z": 64.67256927490235
            },
            "speed": 7.054291248321533
        },
        {
            "timestamp": "2024-11-27T13:27:05.2780414-06:00",
            "position": {
                "x": 36.803077697753909,
                "y": 4.76837158203125e-7,
                "z": 67.50764465332031
            },
            "speed": 3.0248091220855715
        },
        {
            "timestamp": "2024-11-27T13:27:06.2803516-06:00",
            "position": {
                "x": 37.77171325683594,
                "y": 4.76837158203125e-7,
                "z": 67.65538787841797
            },
            "speed": 0.0
        },
        {
            "timestamp": "2024-11-27T13:27:07.2819385-06:00",
            "position": {
                "x": 37.77171325683594,
                "y": 4.76837158203125e-7,
                "z": 67.65538787841797
            },
            "speed": 0.0
        },
        {
            "timestamp": "2024-11-27T13:27:08.2820550-06:00",
            "position": {
                "x": 37.77171325683594,
                "y": 4.76837158203125e-7,
                "z": 67.65538787841797
            },
            "speed": 0.0
        },
        {
            "timestamp": "2024-11-27T13:27:09.2824755-06:00",
            "position": {
                "x": 40.1824951171875,
                "y": 4.76837158203125e-7,
                "z": 66.51229858398438
            },
            "speed": 6.522594451904297
        },
        {
            "timestamp": "2024-11-27T13:27:10.2835076-06:00",
            "position": {
                "x": 46.6827392578125,
                "y": 4.76837158203125e-7,
                "z": 62.11183166503906
            },
            "speed": 8.001322746276856
        },
        {
            "timestamp": "2024-11-27T13:27:11.2850444-06:00",
            "position": {
                "x": 53.08797073364258,
                "y": 4.76837158203125e-7,
                "z": 57.31328582763672
            },
            "speed": 7.999965190887451
        },
        {
            "timestamp": "2024-11-27T13:27:12.2865330-06:00",
            "position": {
                "x": 59.41032028198242,
                "y": 4.76837158203125e-7,
                "z": 52.511817932128909
            },
            "speed": 7.110881328582764
        },
        {
            "timestamp": "2024-11-27T13:27:13.2869423-06:00",
            "position": {
                "x": 62.95216751098633,
                "y": 4.76837158203125e-7,
                "z": 49.126312255859378
            },
            "speed": 2.4827935695648195
        },
        {
            "timestamp": "2024-11-27T13:27:14.2868176-06:00",
            "position": {
                "x": 63.338768005371097,
                "y": 4.76837158203125e-7,
                "z": 48.68126678466797
            },
            "speed": 0.0
        },
        {
            "timestamp": "2024-11-27T13:27:15.2891556-06:00",
            "position": {
                "x": 63.338768005371097,
                "y": 4.76837158203125e-7,
                "z": 48.68126678466797
            },
            "speed": 0.0
        }
    ]
}
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
