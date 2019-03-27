cmds = ""
keyWord = "aci"
rowLen = 5
keyWordLen = len(keyWord)


def getDirection(keyWord, keyWordLen, rowLen, cmds, indx):
        # check whether the char is the begining character
    if(indx == 0):
        preVal = 97
    else:
        preVal = ord(keyWord[indx-1])

    asciiVal = ord(keyWord[indx])

    dif = abs(asciiVal-preVal)
    quotient = dif//rowLen      # 'd'/'u'
    remainder = dif % rowLen    # 'r'/'l'

    # check the direction
    if(asciiVal > preVal):
        # forward direction
        cmds = cmds + ("d" * quotient) + ("r" * remainder) + "!"
    else:
        # reverse direction
        cmds = cmds + ("u" * quotient) + ("l" * remainder) + "!"

    indx += 1
    # return the cmds if all the chars in keyWord is finished
    if(indx >= keyWordLen):
        return cmds

    return getDirection(keyWord, keyWordLen, rowLen, cmds, indx)


print(getDirection(keyWord.lower(), keyWordLen, rowLen, cmds, 0))
