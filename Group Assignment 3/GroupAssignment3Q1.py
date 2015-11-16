def problem1():
    maximum = 0
    for i in range(0, len(arr)):
        current = 0
        for j in range(i, len(arr)):
            current += arr[j]
            if current > maximum:
                maximum = current
    return maximum
