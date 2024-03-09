from flask import Flask, render_template, request, jsonify
from rubi import Rubi
from decouple import config

app = Flask(__name__)
rubi = Rubi()

@app.route('/')
def index():
    return render_template('index.html', context={'aws_acess_key_id': config('AWS_ACCESS_KEY_ID'),
                                                'aws_acess_secret_key': config('AWS_SECRET_ACCESS_KEY'),
                                                'aws_region_name': 'sa-east-1'})

@app.route('/conversation', methods=['POST'])
def conversation():
    data = request.json
    pergunta = data['pergunta']
    resposta = rubi.generate_content(pergunta)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=False)

