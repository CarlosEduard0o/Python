arq = open("disciplina.txt", "r")
arq_saida = open("texto.txt", "w")
for linha in arq:
    lista = linha.rstrip("\n").split() #Pega a linha, tira o \n e da um espaço.
    media = (int(lista[1]) + int(lista[2]))/2 #Depois de ter separado na linha acima, nota 1 fica na posição 1 e nota 2 fica na posição 2
    if media >= 70.0:
        situacao = "Aprovado"
    elif media >= 30.0:
        situacao = "Em exame"
    else:
        situacao = "Reprovado"    
    #print(lista[0], lista[1], lista[2], media, situacao)
    saida = linha.rstrip("\n") + " " + str(media) + " " + situacao + "\n"
    arq_saida.write(saida)

arq.close 
arq_saida.close()



""" arqLeitura = open("testeR.txt", "r")      
arqEscreve = open("testeW.txt", "w")
for linha in arqLeitura:
    lista = linha.rstrip("\n").split()
    media = (int(lista[1]) + int(lista[2]))/2
    if media >= 70.0:
        situacao = "Aprovado"
    elif media >= 30.0:
        situacao = "Em exame"
    else:
        situacao = "Reprovado"
    saida = linha.rstrip("\n") + " " + str(media) + " " + situacao + "\n"            
    arqEscreve.write(saida)
arqLeitura.close
arqEscreve.close  """   