# CaseLeoo
Gabriel Celestino de Souza

# API Rick and Morty

Este script realiza uma requisição à API pública de Rick and Morty utilizando o paradigma ETL para **extrair**, **transformar** e **carregar** dados dos personagens em um arquivo CSV.

## Teste da API no Postman
![Teste Postman](Imagem/Postman.png)

## Requisitos

- **Python 3.7** ou superior.
- Bibliotecas utilizadas:
  - `requests`: Para fazer requisições HTTP e consumir a API.
  - `csv`: Para gravar os dados extraídos em um arquivo CSV.

## Estrutura do Projeto

- **Imagem**: Pasta com prints do script.
- **config.py**: Arquivo com as configurações utilizadas no código principal.
- **RickAndMorty.py**: Arquivo principal que contém o código de extração, transformação e carregamento de dados.

## Funcionamento

### Extract
- Função responsável por consumir a API, verificando se existe uma conexão e fazendo o controle das páginas até que todos os dados necessários sejam coletados. Os dados são armazenados em formato JSON.
- A função realiza requisições paginadas, garantindo que todos os dados sejam extraídos até o limite configurado.
![Extração](Imagem/Extract.png)

### Transform
- Função que trata e filtra os dados extraídos. Ela seleciona apenas os campos necessários, como `id`, `name`, `status`, `species`, `type`, e `gender`, utilizando **dictionary comprehension** para tornar o código mais conciso e fácil de entender.
![Transformação/Tratamento](Imagem/Transform.png)

### Load
- Função responsável por carregar os dados transformados em um arquivo CSV. Ela verifica e escreve as informações no formato desejado, com as colunas separadas por ponto e vírgula (`;`).
![Carregamento](Imagem/Load.png)


