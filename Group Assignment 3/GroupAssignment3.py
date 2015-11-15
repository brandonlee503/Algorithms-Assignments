def crossingMagicalSubsequence(arr, a, middle, b):
    totalSum = 0
    leftSum = 0
    rightSum = 0

    for i in range(a, middle):
        totalSum += arr[i]
        if totalSum > leftSum:
            leftSum = totalSum

    totalSum = 0

    for i in range(middle + 1, b):
        totalSum += arr[i]
        if totalSum > rightSum:
            rightSum = totalSum

    return leftSum + rightSum

def mostMagicalSubsequence(arr, a, b):
    # Only one element
    if a == b:
        return arr[a]

    middle = (a + b) / 2

    # Return the maximum of 3 possible cases
    return max(mostMagicalSubsequence(arr, a, middle),
               mostMagicalSubsequence(arr, middle + 1, b),
               crossingMagicalSubsequence(arr, a, middle, b)
    )

def main():
    arr = [1,2,3,4,5]
    n = len(arr)/arr[0]
    maxSum = mostMagicalSubsequence(arr, 0, n-1)
    print(maxSum)
