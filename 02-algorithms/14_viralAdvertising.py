
import math


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    people = 5
    cum = 0
    for i in range(0, n):
        people = math.floor(people / 2)
        cum += people
        people *= 3
    return cum


