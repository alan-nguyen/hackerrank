
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))

# Second option
# print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
# print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))


