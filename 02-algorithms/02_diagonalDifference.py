def diagonalDifference(arr):
    """Calculate the absolute difference between the sums of a square matrix,  diagonals.
 """
    size = len(arr)
    left_dia = 0
    right_dia = 0

    for i, j in zip(range(0, size), range(size - 1, -1, -1)):
        left_dia += arr[i][i]
        right_dia += arr[i][j]
    diff = abs(left_dia - right_dia)
    return diff


# test case
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))  # Should be 15