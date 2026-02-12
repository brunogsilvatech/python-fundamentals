frase = input("frase favorita: ")
contador = 0
for letra in frase:
    if letra != " ":
        contador = contador + 1
print(contador)