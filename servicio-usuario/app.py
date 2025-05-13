from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/usuarios')
def obtener_usuarios():
    return jsonify([
        {"id": 1, "nombre": "Noel"},
        {"id": 2, "nombre": "Owen"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)