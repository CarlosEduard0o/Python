""" arq = open("disciplina.txt", "r")
letras = []
contador = []
carac = arq.read(1)
while carac:
    if carac != "\n":
        try:
            pos = letras.index(carac)                
        except:
            letras.append(carac)
            contador.append(1)
        else:        
            contador[pos] += 1
    carac=arq.read(1)        
tam = len(contador)   #O resto é para printar a saída
i = 0
while i < tam:
    print(letras[i], contador[i])
    i += 1    
 """

arq = open("disciplina.txt", "r")
for linha in arq:
    lista = linha.rstrip("\n").split() #Pega a linha, tira o \n e da um espaço.
    media = (int(lista[1]) + int(lista[2]))/2 #Depois de ter separado na linha acima, nota 1 fica na posição 1 e nota 2 fica na posição 2
    if media >= 70.0:
        situacao = "Aprovado"
    elif media >= 30.0:
        situacao = "Em exame"
    else:
        situacao = "Reprovado"    
    print(lista[0], lista[1], lista[2], media, situacao)
arq.close        