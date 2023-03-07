string = "Carlos Eduardo"
caractere_repetido = {}

for cont in string:
    if cont in caractere_repetido:  #Verifica se cont está em caractere_repetido
        caractere_repetido[cont] += 1
    else:
        caractere_repetido[cont] = 1
        
print("Caracteres repetidos na string '" + string + "':")
print(caractere_repetido)