num = 6
binRep = nextNum = bin(num)[2:]
binLen = len(binRep)-1


def nextSparse(indx, nextNum, count):
    if(binRep[indx] == '1'):
        count += 1              # count for the consecutive 1's
    else:
        if(count >= 2):
            nextNum = binRep[:indx] + bin(1 << (binLen-indx))[2:]  # clear bit till next 0
            return nextSparse(indx-1, nextNum, 1)
        count = 0

    if(indx == 0):
        if(count >= 2):             #check for MSB
            return (1 << (binLen+1))
        return int(nextNum, 2)

    indx -= 1

    return nextSparse(indx, nextNum, count)


print(nextSparse(binLen, nextNum, 0))
