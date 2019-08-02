def beautifulDays(i, j, k):
    beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
    return (sum(beautifulDays))


