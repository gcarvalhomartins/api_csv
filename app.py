from flask import Flask,jsonify,request
from construct_csv import tratando_Csv

app = Flask(__name__)

corpo_csv = {
    "cabecalho": ["name","mago","mago1"],
    "linhas": ["gabrie","mago2","mago3"]
}

@app.route('/teste',methods=['GET'])
def hello_word():
    return jsonify(corpo_csv)

@app.route('/ccsv',methods=['POST'])
def create_csv():
    novo_csv = request.get_json()
    novo_csv = tratando_Csv(novo_csv)
    return novo_csv

app.run(host='localhost', port=3030, debug=True)
