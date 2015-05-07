def scoreFromFile(txtFileName, dictFileName):
    dictF = open(dictFileName)
    line = dictF.readline()
    D = {}
    L = line.split(' ')
    D[L[0]] = L[1]
    while line:
        L = line.split(' ')
        D[L[0]] = L[1]
        
        
    score = 0
    txtF = open(txtFileName)
    line = txtF.readline()
    txt = ''
    while line:
        words = line.split(' ')
        for w in words:
            smallW = w.lower()
            if smallW in D: score += D[smallW]
    return score

print scoreFromFile('doc0.txt', 'words_dict1.tsv')