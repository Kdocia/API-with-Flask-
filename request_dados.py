import requests
import json

# URL da API
url = 'http://localhost:5000/calculos'

# Dados para a solicitação POST em formato JSON
dados_fatorial = {
    "operacao": "fatorial",
    "valor": 6
}


# Configurando o cabeçalho Content-Type como application/json
headers = {'Content-Type': 'application/json'}

# Fazendo a solicitação POST com headers
response = requests.post(url, json=dados_fatorial, headers=headers)

if response.status_code == 200:
    resultado = response.json()['resultado']
    print(f"Resultado Fatorial: {resultado}")
else:
    print(f"Erro: {response.text}")

dados_fibonacci = {
    "operacao": "fibonacci",
    "valor": 6
}

response = requests.post(url, json=dados_fibonacci, headers=headers)

# Verificando o resultado da solicitação
if response.status_code == 200:
    resultado = response.json()['resultado']
    sequencia = response.json()['sequencia']
    print(f"Termo Fibonacci: {resultado}\nSequência Fibonacci: {sequencia}")
else:
    print(f"Erro: {response.text}")