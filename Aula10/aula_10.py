# Abrindo arquivos pelo python

# "with" garante que o arquivo sera fechado
# "dados.txt" nome do Arquivo
# "w" modo de escrita
# arqvo.write() escreve dentro arquivo
# open("nota.txt", "w")
# "r" modo leitura
# ".read()" le todo o conteudo 
# Abrir um arquivo e Digitar informacoes
# Adicionando conteudo sem apagar
# "a" append (adiciona n ofinal)
# \n quabra de linha




with open("Aula10/nota.txt", "w") as nota_aluno:
    nota_aluno.write("Ola Mundo")

# ler arquivo
with open("Aula10/nota.txt", "r") as leitura_arquivo:
    recebe_texto = leitura_arquivo. read()
    print(recebe_texto)

# Adicionar um texto ao final do seu arquivo
with open("Aula10/nota.txt", "a") as adiciona_novo_texto:
    adiciona_novo_texto.write("\n Aqui tem uma nova linha de texto")



