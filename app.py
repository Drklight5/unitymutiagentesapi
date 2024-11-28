from flask import Flask, jsonify, request, Response
import matplotlib.pyplot as plt
import io
import base64
# import mysql.connector

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def grafica_prueba():
    # Datos de prueba
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 30, 25]

    # Crear la gráfica
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Datos de prueba')
    plt.title('Gráfica de Prueba')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid(True)

    # Guardar la imagen en memoria
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Devolver la imagen como respuesta
    return Response(buf.getvalue(), mimetype='image/png')

@app.route('/', methods=['GET'])
def saludo():
    return "Hola", 200


if __name__ == '__main__':
    app.run(debug=True)
