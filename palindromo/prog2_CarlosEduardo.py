palavra = "Luz azul Luz azul"
i = 0
texto = ""
texto1= ""
j = len(palavra) - 1
cont = len(palavra) - 1
while i <= cont:
    if (palavra[j] != " "):
        texto = texto + palavra[j]
    i += 1
    j -= 1

i = 0
cont = len(palavra) - 1
while i <= cont:
    if (palavra[i] != " "):
        texto1 = texto1 + palavra[i]
    i+=1

texto = texto.lower()
texto1 = texto1.lower()
if (texto == texto1):
    print("É palíndromo")
else:
    print("Não é palíndromo")    
print(texto)    
print(texto1)    