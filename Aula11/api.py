import requests 

# API
url = "https://rickandmortyapi.com/api/character"

resposta = requests.get(url)  # retorno do status 200

print(resposta)

json = resposta.json()  #retornar o JSON

print(json)

personagem = json["results"] # Consulta os meus personagem

print(personagem)

# laço de repetiçao para consultar apenas os nomes dos personagens

for nome_personagem in personagem:
    print(nome_personagem["name"])

# retornar mais informaçoes alem do nome
for mais_info in personagem:
    print("Nome: ", mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especies: ", mais_info["species"])
    print("-----------------------------------")

# pedir ao usuario para digitar um ID e retornar da API o personagem referente a esse ID
id = int(input("Digite um número inteiro: "))

link_API = f"https://rickandmortyapi.com/api/character/{id}"

resposta = requests.get(link_API)
novo_json = resposta.json()

print("Nome: ", novo_json["name"])
print("Status: ", novo_json["status"])
print("Especies: ", novo_json["species"])
print("-----------------------------------")

# Data para entrega: 15/03/2026
# criar um menu para a selecao
# 1- consultar por id
# 2- consultar por nome
# 3- lista de personagem

# se for opcao 1:
""""
pedir ao usuario para digitar um ID(numero inteiro) e retornar de dentro da API o personagem referente ao nome digitado
"""

# se for opcao 2:
""""
pedir ao usuario digitar um nome e retornar o resultado

OBS de codigo: para percorrer o json e retornar o nome digitado:
"""


# se for opcao 3:
# retornar todos os personagem
# lista de informaçoes que deverão ser retornadas:

