arq = open("disciplina.txt", "r")

# Lendo todas as linhas de um arquivo texto
print("Listando com WHILE")
linha = arq.readline()
while linha:
    print(linha.rstrip("\n"))
    linha = arq.readline()

# Ou assim   
print("Listando com FOR")
arq.seek(0) # Posiciona o ponteiro de arquivo (apontador) apontando para o Byte 0 (primeiro).
for linha in arq:
    print(linha.rstrip("\n"))

# Ou ainda lendo todas as linhas de uma só vez gerando uma lista de linhas
print("Listando utilizando LISTA")
arq.seek(0)
lista = arq.readlines()
for linha in lista:
    print(linha.rstrip("\n"))

arq.close()

     

#Se abrir o arquivo para leitura, ele tem que existir (r)    

#while linha: Faz enquanto tiver conteudo no arquivo

#print (10, end = "\n") para pular linha, é o mesmo que print (10, end = ""), pois \n é default

#rstrip serve para eliminar o  caractere que está a direita da string print(linha.rstrip("\n"))

#Se não fizer o rstrip, o print pula linha duas vezes


#Se fechar e abrir o arquivo, automaticamente o ponteiro vai para zero. O arq.seek(0) arq é minha variável,
#.seek é a função. O arq.seek(0) serve para reposicionar o ponteiro em 0 sem ter que fechar e abrir o arquivo

#for linha in arq:
#Com for, o python automaticamente já entende que é cada linha.

#lista = arq.readlines()
#for linha in lista:   Para cada linha do arquivo

#read(1) le de 1 em 1 caractere
#pos = caracteres.index(carac) retorna a posição
