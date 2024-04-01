import csv

teste_json = {
    "cabecalho" : ["valor","valor2","valor3"]
}

def tratando_Csv(receive_json):
    receive_json.keys()
    receive_json = receive_json['cabecalho']
    return receive_json


def create_body_csv(heade_csf):
    heade_csf = tratando_Csv(heade_csf)
    with open('testando.csv', mode='w', newline = '') as csv_file:
        cabecalho = heade_csf

        writer = csv.DictWriter(csv_file,fieldnames=cabecalho)
        writer.writeheader()
        writer.writerow({"Mago1":"Oi","Mago2":"Sou o Mago","Mago3":"hehehehe"})

create_body_csv(teste_json)