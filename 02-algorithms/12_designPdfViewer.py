def designerPdfViewer(h, word):
    h = [int(i) for i in h.split()]
    word = [h[ord(c)-ord('a')] for c in word]
    return max(word) * len(word)


