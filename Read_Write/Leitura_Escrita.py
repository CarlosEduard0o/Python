LerArquivo = open("testeRead.txt", "r")
EscreverArquivo = open("testeWrite.txt", "w")
for linha in LerArquivo:
    linha_1 = linha.rstrip("\n").split()    #rstrip tira fora o espaço causado pelo enter. Split separa tudo o que estiver separado entre o parametro do split
    print(linha_1[2])                       #Mostra a palavra da posição 2
    #print(linha[2])                         #Mostra a letra da posição 2    
    #EscreverArquivo.write(str(linha_1))
LerArquivo.close 
EscreverArquivo.close