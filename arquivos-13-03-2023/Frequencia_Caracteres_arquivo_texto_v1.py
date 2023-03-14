arq = open("disciplina.txt", "r")

caracteres = [] #Lista para fazer o comparador (Armazena letras por letras para comparar com o arquivo)
frequencia = [] #Armazena a frequência
carac = arq.read(1) # O método read(1) le apenas um caracter (1 byte) por vez.
while carac: #Enquanto houver conteúdo no arquivo carac
    if carac != "\n": #Como estou lendo caractere por caractere, tenho que colocar uma condição para entender quando pula linha
        try:    #Tenta fazer com que pos receba a posição carac
            pos  = caracteres.index(carac)          
        except: #Se a condição do try não for possível, executa o except
            caracteres.append(carac)    #Acrescenta carac
            frequencia.append(1)        #Adiciona 1
        else: #Executa o else se a condição do try não der erro
            frequencia[pos] += 1        #Contador
    carac = arq.read(1)         #Lê o próximo caractere

tam = len(frequencia)   #O resto é para printar a saída
i = 0
while i < tam:
    print(caracteres[i], frequencia[i])
    i += 1