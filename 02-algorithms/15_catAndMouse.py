def catAndMouse(x, y, z):
    catA = abs(x - z)
    catB = abs(y - z)
    if catA > catB:
        return 'Cat B'
    elif catA < catB:
        return 'Cat A'
    else:
        return'Mouse C'


# test case
print(catAndMouse(6, 1, 4))  # Should be Cat A
print(catAndMouse(1, 5, 4))  # Should be Cat B
print(catAndMouse(3, 9, 6))  # Should be Mouse C