def hurdleRace(k, height):
    if k >= max(height):
        return 0
    else:
        return max(height) - k


# test case
h = [1,3,4,5,2,5]
print(hurdleRace(3, h))  # Should be 2
print(hurdleRace(8, h))  # Should be 0