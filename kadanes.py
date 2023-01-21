def kadanes(arr):
    maxSum = arr[0]

    currSum = 0
    for n in range(len(arr)):
        currSum = max(currSum, 0)
        currSum += arr[n]
        maxSum = max(maxSum, currSum)
    
    return maxSum

print(kadanes([1,-2,4,-5,5,6]))