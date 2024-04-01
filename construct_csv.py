import csv
import json

teste_json = {
    "cabecalho" : ["Mago1","Mago2","Mago3"],
    "linhas" : {"Mago1":"Oi","Mago2":"Sou o Mago","Mago3":"hehehehe"}
}


def tratando_Header_Csv(receive_json):
    receive_json = receive_json['cabecalho']
    return receive_json

def rows_csv(receive_json_rows):
    receive_json_rows = receive_json_rows['linhas']
    return receive_json_rows


def create_body_csv(recebendo_json):

    heade_csf = tratando_Header_Csv(recebendo_json)
    body_csv = rows_csv(recebendo_json)

    with open('testando.csv', mode='w', newline = '') as csv_file:
        cabecalho = heade_csf

        writer = csv.DictWriter(csv_file,fieldnames=cabecalho)
        writer.writeheader()
        writer.writerow(body_csv)
    recebendo_json = csv_file

    return recebendo_json


