
inArr = [2, 5, 6, 7, 8, 8, 9]
target = 4

def whereIsTarget(arr, target, left, right):
    while left <= right:
        mid = int((left+right)/2)

        if arr[mid] == target:
            return arr[mid]

        # search left half
        elif target < arr[mid]:
            right = mid - 1

        # serach right half
        else:
            left = mid + 1

    # if the mid is at the end
    if(mid != len(arr)-1):
        if(target-arr[mid] > arr[mid+1]-target):
            return arr[mid+1]
    else:
        if(target-arr[mid] < arr[mid-1]-target):
            return arr[mid-1]
    return arr[mid]


print(whereIsTarget(inArr, target, 0, len(inArr)-1))
