from flask import Flask, render_template, request, jsonify
from rubi import Rubi

app = Flask(__name__)
rubi = Rubi()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversation', methods=['POST'])
def conversation():
    data = request.json
    pergunta = data['pergunta']
    resposta = rubi.generate_content(pergunta)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)

