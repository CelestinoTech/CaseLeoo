import requests  
import csv  
from config import LIMITE, ENDPOINT

def extract():
    dados = []  
    page = 1  
    while len(dados) < LIMITE:
        req = requests.get(ENDPOINT, params={"page": page})
        if req.status_code != 200: 
            print("Erro de conexão com o ENDPOINT")
            break
        else:
            data = req.json() 
            resultado = data.get("results", [])  
            if not resultado:
                print("Sem resultados")  
                break
            dados.extend(resultado)  
            page += 1  
    return dados

def transform(dados_brutos):
    dados_transformados = []
    for i in dados_brutos:
        if len(dados_transformados) >= LIMITE:
            break
        dados_transformados.append({key: i[key] for key in i.keys()
                                    & {"id", "name", "status", "species", "type", "gender"}})
    return dados_transformados

def load(dados, nome_arquivo="personagens.csv"):
    colunas = ["id", "name", "status", "species", "type", "gender"]
    with open(nome_arquivo, mode="w", newline="") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";", quotechar='"')  
        escritor.writerow(colunas)
        for dado in dados:
            escritor.writerow([dado[coluna] for coluna in colunas])

dados_brutos = extract() 
personagens = transform(dados_brutos)  
load(personagens)  
print("Dados salvos em 'personagens.csv' com sucesso!")
