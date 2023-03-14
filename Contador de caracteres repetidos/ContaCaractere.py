word = "Chocolate"                                            #Input
ComparaPalavra = []                                           #Vetor criado para fazer a comparação
ArmazenaPalavra = []                                          #Vetor criado para contar os caracteres repetidos  
tamW = len(word)                                              #Variável que recebe o tamanho da string para o while  
i = 0                                                         #Variável para o loop  
while i < tamW:                                               #Loop até varrer toda a palavra  
    tamC = len(ComparaPalavra)                                #Nova variável criada para sempre receber o tamanho do vetor comparador  
    j = 0                                                     #Nova variável para loop  
    while j < tamC and word[i] != ComparaPalavra[j]:          #Condição do loop  
        j+=1                                                  #Contador do loop  
    if j < tamC:
        ArmazenaPalavra[j] += 1
    else:
        ComparaPalavra.append(word[i])
        ArmazenaPalavra.append(1) 
    i+=1
tamC = len(ComparaPalavra)
i = 0
while i < tamC:
    print(ComparaPalavra[i], ArmazenaPalavra[i])
    i+=1

        