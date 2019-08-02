def designerPdfViewer(h, word):
    h = [int(i) for i in h.split()]
    word = [h[ord(c)-ord('a')] for c in word]
    return max(word) * len(word)


# test case
#h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7"
word = 'abc'
print((designerPdfViewer(h, word)))