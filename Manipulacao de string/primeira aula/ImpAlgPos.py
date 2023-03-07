def POS (cadeia, subcadeia):
    tamc = len(cadeia)
    tams = len(subcadeia)
    achou = 0
    #local = 0
    if (tamc >= tams):
        inicio = 0
        while (tamc >= tams) and (achou == 0):
            i = 0
            j = inicio
            if (subcadeia[i] == cadeia[j]):
                local = j
                i += 1
                j += 1
                while (i < tams) and (subcadeia[i] == cadeia[j]):
                    i += 1
                    j += 1
                if (i < tams):
                    inicio += 1
                    tamc += 1
                else:
                    achou = 1   
            else:
                inicio += 1
                tamc -= 1
    else:
        print("A subcadeia tem tamanho maior que a cadeia! ")
    if (achou == 0):
        local = -1       
    return local    


cadeia = input("Digite um nome: ")
subcadeia = input("Digite o caractere que você deseja saber a posição: ")
print(POS(cadeia, subcadeia))                     
            