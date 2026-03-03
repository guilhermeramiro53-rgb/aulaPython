print("Digite 5 nota: ")

notas=[]

for i in range(5):
    nota = int(input("Digite a nota:"))
    notas.append(nota)
media = sum(notas) / len(notas)
print("A média é:", media)
if media >=5: 
    print("Aprovado")
else:
    print("Reprovado")