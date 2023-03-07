palavra = "casa"
i = 0
texto = ""
texto1= ""
j = len(palavra) - 1
cont = len(palavra) - 1
while i <= cont:
    texto = texto + palavra[j]
    i += 1
    j -= 1

i = 0
cont = len(palavra) - 1
while i <= cont:
    texto1 = texto1 + palavra[i]
    i+=1


if (texto == texto1):
    print("É palíndromo")
else:
    print("Não é palíndromo")    
#print(texto)    
#print(texto1)    