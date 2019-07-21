def compareTriplets(a, b):
    """Comparing each element of a and b"""
    a_score = 0
    b_score = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
        else:
            a_score = a_score
            b_score = b_score
    result = [a_score, b_score]
    return result


# test case
a = [5, 6, 7]
b = [3, 6, 10]
compareTriplets(a, b)