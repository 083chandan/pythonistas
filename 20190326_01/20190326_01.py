wordsSet = ["vil", "sit", "flick", "pat", "pluck", "sat", "vat"]
inputWrd = "vit"

suggWrds = []
count = 0


def suggestedWords(wordsSet, count, indx, suggWrds):
    i = 0
    misMatchCnt = 0
    newSetWrd = wordsSet[indx] if len(inputWrd) == len(wordsSet[indx]) else ""
    while (i < len(newSetWrd) and misMatchCnt < 2 and newSetWrd != ""):
        if inputWrd[i] != newSetWrd[i]:
            misMatchCnt += 1
        i += 1
    if(misMatchCnt == 1):
        suggWrds.append(newSetWrd)
        count += 1

    indx += 1
    if(count == 3 or indx >= len(wordsSet)):
        return suggWrds
    return suggestedWords(wordsSet, count, indx, suggWrds)


print(suggestedWords(wordsSet, count, 0, suggWrds))
