def triangleQuest(n):
    """ Print a numerical triangle of height n - 1,
     using only arithmetic operations and a single for loop
     """
    for i in range(1, n):
        print((10**(i)//9)*i)


# test case
triangleQuest(5)

triangleQuest(10)
