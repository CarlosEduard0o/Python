word = "Chocolate"
WordTwo = []
StoreWord = []
i = 0
TamW = len(word)
while i < TamW:
    TamWT = len(WordTwo)
    j = 0
    #print("Tamanho da WordTwo: ", TamWT)
    while j < TamWT and word[i] != WordTwo[j]:
        j += 1
        print("oi")
        print("Tamanho da WordTwo: ", TamWT)    
    if j < TamWT:
        StoreWord[j] += 1      
        #print("Tamanho da WordTwo: ", TamWT)    
    else:
        WordTwo.append(word[i])
        StoreWord.append(1)
        #print("Tamanho da WordTwo: ", TamWT)
    print("oi 2")    
    i += 1    