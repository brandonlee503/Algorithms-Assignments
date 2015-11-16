# The following is a pseudocode implementation that isn't expected to properly compile.
def problem1(arr):
    mostMagicalSubsequence = []
    maximumValue = 0

    for i in range(0, n):
        for j in range(i, n):
            currentSubsequence = arr[i:j+1]
            currentValue = min(currentSubsequence) * sum(currentSubsequence)
            if currentValue > maximumValue:
                mostMagicalSubsequence = currentSubsequence
    return mostMagicalSubsequence

# The algorithm problem1() runs in O(n^2) time as it takes in an n size array
# and checks every element i for a possible most magical subsequence for each
# length j. In our pseudocode above, this checking is achieved using two for
# loops (nested), which results in O(n^2) runtime. The subsequence check is
# implemented by checking the minimum element in the subsequence with the sum of
# the subsequence. Finally an if statement is used to check for which subsequence
# has a greater value. This runs in O(1) time. Thus we obtain O(n^2) * O(1) = O(n^2).
