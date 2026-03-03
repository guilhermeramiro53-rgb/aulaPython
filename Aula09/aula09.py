nome = "Beltrano"

# Parametros sempre vão dentro do parenteses
def saudacao ():
    print("Olá", nome ,"Seja Bem-Vindo")

# chamar uma funçao
saudacao()

#recebe dois valores, faz a soma e retorna o resultado
def soma(valor1, valor2):
    return valor1 + valor2

print(soma(1445, 666))

salario_funcionario = 1600
beneficio = 200
novo_salario = soma(salario_funcionario,beneficio)
print(novo_salario)

#soma dois valores se a idade for igual ou maior que 18
#senao mostrar mensagem sua idade e menor 18
idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= 18:
    var1 = int(input("Digite o primeiro valor: "))
    var2 = int(input("Digite o primeiro valor: "))
    resultado = soma(var1, var2)
    print(resultado)
else:
    print("Sua idade é menor que 18")

lista = [20, 1, 9, 11, 35]
#Retornar a quantidade de informaçoes contidas em uma variavel
print(len(lista))

#SUM - soma toda a minha lista numerica
print(sum(lista))

# MAX 
print("Maior", max(lista))
# MIN
print("Menor", min(lista))

#ORDERNAR
print(sorted(lista))

#TYPE - TIPO
tipo = 20
print(type(tipo))

print(float(tipo))

