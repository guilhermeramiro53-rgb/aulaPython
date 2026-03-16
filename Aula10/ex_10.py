cadastros = []

print("=== Sistema de Cadastro ===")

while True:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    cadastros.append(pessoa)
    print("Cadastro realizado com sucesso!\n")

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()
    if continuar != 's':
        break

print("\n=== Pessoas cadastradas ===")
for p in cadastros:
    print(f"Nome: {p['nome']} - Idade: {p['idade']}")

with open("cadastros.txt", "a") as arquivo:
    arquivo.write(nome + "-" + idade + "\n")