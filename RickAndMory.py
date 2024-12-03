import requests  
import csv  

LIMITE = 50
ENDPOINT = "https://rickandmortyapi.com/api/character/"

def requisicao():
    dados = []  
    page = 1  # A API retorna 20 personagens por página. A variável permite avançar as páginas.

    while len(dados) < LIMITE:
        req = requests.get(ENDPOINT, params={"page": page})
        if req.status_code != 200: 
            print("Erro de conexão com o ENDPOINT")
            break
        else:
            data = req.json() 
            resultado = data.get("results", [])  
            if not resultado:  
                break
            for i in resultado:
                if len(dados) >= LIMITE:
                    break
                dados.append({
                    "id": i ["id"],
                    "name": i ["name"],
                    "status": i ["status"],
                    "species": i ["species"],
                    "type": i ["type"],  
                    "gender": i ["gender"]
                })
            page += 1  # Avança para a próxima página 
    return dados

def salvar_csv(personagens, nome_arquivo="personagens.csv"):
    # Abre um arquivo do tipo CSV
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo,delimiter=";")  
        # Cria os cabeçalhos
        escritor.writerow(["ID", "Nome", "Status", "Espécie", "Tipo", "Gênero"])

        # Intera cada personagem e escreve
        for personagem in personagens:
            escritor.writerow([
                personagem["id"],
                personagem["name"],
                personagem["status"],
                personagem["species"],
                personagem["type"],
                personagem["gender"]
            ])

# "MAIN"
personagens = requisicao()
salvar_csv(personagens)
print("Dados salvos em 'personagens.csv' com sucesso!")
