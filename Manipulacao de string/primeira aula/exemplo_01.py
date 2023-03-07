nome = "Carlos Eduardo de Almeida Rosa"
print(nome[0])
print(nome[-7])  #7 de trás para frente
print(nome[2:5]) #Posição 2 até a posição 4
print(nome.count("r")) #Conta quantos r tem na string
print(nome.count("ar")) #Posso colocar até mais de uma letra
print(nome.find("C")) #Mostra a posição do caractere. Quando não encontra mostra -1
print(nome.find("ei")) #Ou posso colocar mais de um caractere. Se houver mais de uma dupla de caractere iguais, vai mostrar o que vier primeiro
lista = nome.split("a") #O split gera como retorno uma lista, com as palavras que ele encontrar separadas pelo parâmetro entre parêntese.
print(lista)
print(lista[1]) #Mostra o segundo elemento do split, que no caso é o Eduardo. Segundo, pois começa em zero.