def breakingRecords(scores):
    m = l = scores[0]
    cm = cl = 0
    for i in scores:
        if i > m:
            cm += 1
            m = i
        if i < l:
            cl += 1
            l = i
    return cm, cl


