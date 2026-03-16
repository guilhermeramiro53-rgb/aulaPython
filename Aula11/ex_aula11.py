
import requests 
url = "https://rickandmortyapi.com/api/character"

resposta = requests.get(url)  

print(resposta)

json = resposta.json()  

print(json)

personagem = json["results"] 

print(personagem)
for nome_personagem in personagem:
    print(nome_personagem["name"])
for mais_info in personagem:
    print("Nome: ", mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especies: ", mais_info["species"])
    print("-----------------------------------")

id = int(input("Digite um número inteiro: "))

link_API = f"https://rickandmortyapi.com/api/character/{id}"

resposta = requests.get(link_API)
novo_json = resposta.json()

print("Nome: ", novo_json["name"])
print("Status: ", novo_json["status"])
print("Especies: ", novo_json["species"])
print("-----------------------------------")

import requests

def buscar_personagem():
    id = int(input("Digite um número inteiro: "))
    link_API = f"https://rickandmortyapi.com/api/character/{id}"
    resposta = requests.get(link_API)
    novo_json = resposta.json()

    print("Nome: ", novo_json["name"])
    print("Status: ", novo_json["status"])
    print("Espécie: ", novo_json["species"])
    print("-----------------------------------")

import requests

def buscar_personagem_por_id():
    id = int(input("Digite o ID do personagem: "))
    link_API = f"https://rickandmortyapi.com/api/character/{id}"
    resposta = requests.get(link_API)
    novo_json = resposta.json()

    print("Nome: ", novo_json["name"])
    print("Status: ", novo_json["status"])
    print("Espécie: ", novo_json["species"])
    print("-----------------------------------")

def buscar_personagem_por_nome():
    nome = input("Digite o nome do personagem: ")
    link_API = f"https://rickandmortyapi.com/api/character/?name={nome}"
    resposta = requests.get(link_API)
    dados = resposta.json()

    if "results" in dados:
        for personagem in dados["results"]:
            print("Nome: ", personagem["name"])
            print("Status: ", personagem["status"])
            print("Espécie: ", personagem["species"])
            print("-----------------------------------")
    else:
        print("Nenhum personagem encontrado com esse nome.")

def menu():
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1 - Buscar personagem por ID")
        print("2 - Buscar personagem por Nome")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            buscar_personagem_por_id()
        elif opcao == "2":
            buscar_personagem_por_nome()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu
menu()