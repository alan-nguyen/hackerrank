def angryProfessor(k, a):

    count = 0

    # counting students on time
    for s in a:
        if s <= 0:
            count += 1

    # Class is not canceled
    if count >= k:
        return False

    # Class is canceled
    else:
        return True


