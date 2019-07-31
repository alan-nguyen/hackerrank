def pickingNumbers(a):
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER_ARRAY a as parameter.
    max = 0
    for i in a:
        c = a.count(i)
        d = a.count(i - 1)
        c = c + d
        if c > max:
            max = c
    return max


# test case
a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
print(pickingNumbers(a))