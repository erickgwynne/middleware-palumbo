"""

from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

PATH_TO_FILE = "/path/to/your/{}.txt"  # Actualiza esto con la ruta correcta

@app.route('/modify_status/<string:id_received>/', methods=['POST'])
def modify_status(id_received):
    if not os.path.exists(PATH_TO_FILE.format(id_received)):
        return jsonify({"error": "El archivo no existe"}), 404

    with open(PATH_TO_FILE, 'r') as file:
        data = json.load(file)

    data['status'] = '1'

    with open(PATH_TO_FILE, 'w') as file:
        json.dump(data, file)

    return jsonify({"message": "Archivo modificado con éxito"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')  # escucha en todas las interfaces

"""
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

URL_BASE = "http://172.173.164.225/Webservices/Comandas/{}.txt"

@app.route('/set_status/<string:id_received>/', methods=['GET'])
def set_status(id_received):

    response = requests.get(URL_BASE.format(id_received))
    
    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener el archivo"}), 500

    data = response.json()
    data['status'] = '1'

    with open(f"{id_received}.txt", 'w') as file:
        file.write(json.dumps(data))

    return jsonify({"message": "Archivo modificado y guardado con éxito"}), 200

if __name__ == "__main__":
    app.run(debug=True)
