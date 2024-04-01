import csv
import json

teste_json = {
    "cabecalho" : ["Mago1","Mago2","Mago3"],
    "linhas" : [{"Mago1":"Oi","Mago2":"Sou o Mago","Mago3":"hehehehe"}]
}


def tratando_Header_Csv(receive_json):
    receive_json.keys()
    receive_json = receive_json['cabecalho']
    return receive_json

def rows_csv(receive_json_rows):
    receive_json_rows.keys()
    receive_json_rows = receive_json_rows['linhas']
    return print(receive_json_rows)

rows_csv(teste_json)

def receive_Json(json_receive):
    heade_csf = tratando_Header_Csv(json_receive)
    body_csv = rows_csv(json_receive)
    return print(heade_csf,body_csv)


def create_body_csv(recebendo_json):
    recebendo_json = receive_Json(recebendo_json)
    heade_csf = tratando_Header_Csv(recebendo_json)
    body_csv = rows_csv(recebendo_json)

    with open('testando.csv', mode='w', newline = '') as csv_file:
        cabecalho = heade_csf

        writer = csv.DictWriter(csv_file,fieldnames=cabecalho)
        writer.writeheader()
        writer.writerow(body_csv)

