import csv

def tratando_Csv(receive_json):
    receive_json.keys()
    receive_json['cabecalho']
    receive_json = create_body_csv(receive_json)
    return receive_json

def create_body_csv(heade_csf):
    with open('testando.csv', mode='w', newline = '') as csv_file:
        cabecalho = [heade_csf]

        writer = csv.DictWriter(csv_file,fieldnames=cabecalho)
        writer.writeheader()
        writer.writerow({"Mago1":"Oi","Mago2":"Sou o Mago","Mago3":"hehehehe"})

