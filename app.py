from flask import Flask,jsonify,request

app = Flask(__name__)

corpo_csv = [{
    "cabecalho": ["name","mago","mago1"],
    "linhas": ["gabrie","mago2","mago3"]
}]

@app.route('/teste',methods=['GET'])
def hello_word():
    return jsonify(corpo_csv)

@app.route('/cc',methods=['POST'])
def create_csv():
    novo_csv = request.get_json()
    print(novo_csv)
    return novo_csv

app.run(host='localhost', port=3030, debug=True)
