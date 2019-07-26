def split_and_join(line):
    """Split and join string with - """
    line_split = line.split(" ")
    line_join = "-".join(line_split)
    return line_join


# test case
line = 'this is a string'
print(split_and_join(line))  # should be  "this-is-a-string"