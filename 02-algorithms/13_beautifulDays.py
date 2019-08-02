def beautifulDays(i, j, k):
    beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
    return (sum(beautifulDays))


# test case
print(beautifulDays(20, 23, 6))  # Should be 2