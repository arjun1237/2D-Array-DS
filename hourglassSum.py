def hourglassSum(arr):
    array_len = len(arr)
    highest = 0
    for i in range(1, array_len-1):
        for j in range(1, array_len-1):
            total = arr[i][j]
            for k in range(0, 3):
                total += arr[i-1][j-1+k] + arr[i+1][j-1+k]
            if i == 1 and j == 1:
                highest = total
            if total > highest:
                highest = total
    return highest

print(hourglassSum(arr))