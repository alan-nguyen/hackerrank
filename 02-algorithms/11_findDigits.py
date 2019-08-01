def findDigits(n):
    r = n
    count = 0
    while r > 0:
        if (r % 10 != 0 and n % (r % 10) == 0):
            count += 1
        r = r // 10
    return count


# test case
print(findDigits(111))  # Should be 3
print(findDigits(12))  # Should be 2
