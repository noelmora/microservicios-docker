from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/pedidos')
def obtener_pedidos():
    # Obtener usuarios desde el servicio de usuarios
    usuarios = requests.get('http://servicio-usuario:5000/usuarios').json()
    pedidos = [
        {"id": 1, "usuario": usuarios[0], "producto": "Monitor"}
    ]
    return jsonify(pedidos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)