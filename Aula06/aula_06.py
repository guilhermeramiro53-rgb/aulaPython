texto1 = "SENAC"
print(texto1[0])
print(texto1[1])
print(texto1[2])
print(texto1[3])
print(texto1[4])

# FUNÇAO LEN()
texto2 = "입니다. 저는 브라질 사람입니다. 만나서 반갑습니다"
print(len(texto2))

# FUNÇAO MAI/MIN
texto3 = "ola mundinho"
print(texto3.upper())

texto4 = "OLA MUNDAO"
print(texto4.lower())

print(texto3.capitalize())

print(texto3.title())

texto5 = "Python"

print(texto5[0:3])
print(texto5[0:5])

# REPLACE
texto6 = "Eu gosto de Java"
novo_texto = texto6.replace("de Java", "Panqueca")
print(novo_texto)

#ESPACO EM BRANCO
texto7 = "  Ola Mundo  "
print(texto7.strip() + "string") # remove esquerda e direita
print(texto7.lstrip() + "string") # remove esquerda
print(texto7.rstrip() + "string") # remove direita 

# METODO STRING
texto8 = "Pulei carnaval, mas hoje estou estudando."
print("CARNAVAL" in texto8)
# CASE SENSITIVE = SENSIVEL a letras maiusculas e minusculas

print(texto8.find("estudando")) # retornar o valor 31
print(texto8[31]) # e

print(texto8.count("a"))

texto9 = "Eu amo Jogos"
print(texto9.startswith("Eu"))
print(texto9.endswith("os"))