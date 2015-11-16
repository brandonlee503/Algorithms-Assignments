# The following is a pseudocode implementation that isn't expected to properly compile.
def problem1(arr):
    mostMagicalSubsequence = []
    maximumValue = 0

    for i in range(0, n):
        for j in range(i, n):
            currentSubsequence = arr[i:j]
            currentValue = min(currentSubsequence) * sum(currentSubsequence)
            if currentValue > maximumValue:
                mostMagicalSubsequence = currentSubsequence
    return mostMagicalSubsequence
