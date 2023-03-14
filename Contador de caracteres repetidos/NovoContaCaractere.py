word = "Chocolate"
WordTwo = []
StoreWord = []
i = 0
TamW = len(word)
while i < TamW:
    TamWT = len(WordTwo)
    j = 0
    while j < TamWT and word[i] != WordTwo[j]:
        j += 1
    if j < TamWT:
        StoreWord[j] += 1      
    else:
        WordTwo.append( )
        StoreWord.append(1)
        print(word[i])
        print(WordTwo)
        print(StoreWord)            
    i += 1    
""" TamWT = len(WordTwo)
j = 0
while j < TamWT:
    print(StoreWord[j])
    j += 1  """ 