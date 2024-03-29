def integersComeInAllSizes(arr):
    """ Calculation on very large integers
    :param arr: four numbers a, b, c and d
    :return: a^b + c^d
    """
    a,b,c,d = (arr[i] for i in range(4))
    print(pow(a,b) + pow(c,d))


# test case
x = [9, 29, 7, 27]
integersComeInAllSizes(x)  # Should be 4710194409608608369201743232
