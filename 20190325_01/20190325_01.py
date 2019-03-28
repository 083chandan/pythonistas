
a = [4, 5, 6, 5, 6, 7, 8, 9, 10, 9, 10]

target = 10
indx = 0


def findFirst(a, indx, target):
    if(a[indx] == target):
        print(indx+1)
        return indx
    else:
        if(a[indx] > target):
            jump = indx - a[indx] - target  # Jump
            return findFirst(a, jump, target)
        else:
            jump = indx + target - a[indx]  # Jump
            return findFirst(a, jump, target)


findFirst(a, indx, target)
