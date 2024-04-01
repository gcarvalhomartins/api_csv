from flask import Flask,jsonify,request
from construct_csv import tratando_Csv, create_body_csv

APP = Flask(__name__)

corpo_csv = {
    "cabecalho": ["name","mago","mago1"],
    "linhas": ["gabrie","mago2","mago3"]
}

@APP.route('/teste',methods=['GET'])
def hello_word():
    return jsonify(corpo_csv)

@APP.route('/ccsv',methods=['POST'])
def create_csv():
    novo_csv = request.get_json()
    novo_csv = create_body_csv(novo_csv)
    return novo_csv

APP.run(host='localhost', port=3030, debug=True)
