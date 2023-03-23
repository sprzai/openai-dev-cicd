from flask import Flask
from openai_function import generate_text, generate_multiple_text

app = Flask(__name__)

# Método GET para obtener una lista de usuarios
@app.route('/send_message/<string:prompt>', methods=['GET'])
def send_message(prompt):
    salida = generate_text(prompt)
    return {'mensaje': salida}

# Método GET para obtener un usuario específico por su ID
@app.route('/send_message2/<string:prompt>', methods=['GET'])
def send_message2(prompt):
    salida = generate_multiple_text(prompt)
    return {'mensaje': salida}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
