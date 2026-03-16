# criar numero aleatorio
# BIBLIOTECA random
# BIBLIOTECA MATH 
import random
import math 
import datetime
numero_aleatorio = random.randint(1000, 2000)

print(numero_aleatorio)
# randint gera apenas numeros aleatorios 
# sorteio de alunos
alunos = ["Israel", "Adenilson", "Wellington", "Jonathan", "Ana", "Isabelly", "João Pedro", "Luis Felipe", "Iara", "Vanessa", "Daniel", "João Paulo", "Lucas", "Bernardo", "Camila", "Stefany", "Guilherme", "Micael", "Kauan"]
sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)
# CHOICE escolher de forma aleatoria
print("Dupla Dinamica", sorteado, "-", sorteado2)

# sqrt raiz quadrada
numero = 32
raiz = math.sqrt(numero)
print(raiz)

# Elevar um numero
print(math.pow(2, 2))

# BIBLIOTECA DATATIME
# Trabalhando com data
agora = datetime.datetime.now()
print(agora.year)

#EXERCICIO
# SOLICITAR AO USUARIO UM NUMERO DE 1 A 5 
# GERAR UM NUMERO ALEATORIO USANDO A BIBLIOTECA RANDOM. RANDINT
# VERIFICAR SE O USUARIO DIGITOU O MESMO VALOR QUE O RESULTADO DA FUNCAO RANDIT

numero_usuario = int(input("Digite um numero da sorte de 1 ate 5:"))
numero_sorte = random.randint(1, 5)
if numero_usuario == numero_sorte:
    print("Parabens fulano, um aperto de mão e 2 reais!")
else:
    print("Errou, tente novamente!")





