string = "teste"
tam = len(string)
letras = []
contagem = []
i = 0
while i < tam:
    taml = len(letras)
    j = 0
    #print(taml)
    #print(j)
    while j < taml and string[i] != letras[j]:
        j += 1
        #print(j)
        #print(string[i])
        #print(letras[j])
    if j < taml:
        contagem[j] += 1
        #print(contagem[j])
    else:
        letras.append(string[i])
        contagem.append(1)
        #print(letras)
        #print(contagem)
    i += 1    

taml = len(letras)
i = 0
while i < taml:
    print(letras[i], contagem[i])
    i += 1