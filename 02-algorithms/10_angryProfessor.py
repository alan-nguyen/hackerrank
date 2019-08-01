def angryProfessor(k, a):
    """
    Given the arrival time of each student and a threshold number of attendees, determine if the class is canceled.
    :param k: int threshold for minimum on time student
    :param a: array of arrival time of students
    :return: Class cancel
    """
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


