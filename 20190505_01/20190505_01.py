# [-3,-2,-1,5,6,7,9,11,12,13,15,16]
# -3--1,5-7,9,11-13,15,16

# numbersIn = "-3 -2 -1 5 6 7 9 11 12 13 15 16"
# numbersIn = numbersIn.strip().split(" ")

numbersIn=(input("Please enter the space seperated numbers.")).strip().split(" ")
numbersList = list(map(int, numbersIn))
numbersList.sort()

indx = 0


def checkCons(numbersList, numberListLen, consNumberList, startNum, indx, prevNum):
    if(indx == numberListLen):
        return(consNumberList)
    count = 0
    while(abs(abs(numbersList[indx])-abs(prevNum)) == 1):
        prevNum = numbersList[indx]
        indx += 1
        count += 1
    if(count > 1):
        consNumberList[-1] = consNumberList[-1]+"-" + str(numbersList[indx-1])
    else:
        consNumberList.append(str(numbersList[indx]))
        indx += 1
    return checkCons(numbersList, numberListLen, consNumberList, numbersList[indx-1], indx, numbersList[indx-1])


print(checkCons(numbersList, len(numbersList)-1,
                [], numbersList[indx], indx, numbersList[indx]))
