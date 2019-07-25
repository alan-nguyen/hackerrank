if __name__ == '__main__':
    # read input
    n = int(input())

    # Split the string by whitespace into a list
    integer_list = map(int, input().split())

    # Convert list to tuple
    t = tuple(integer_list)

    # print hash table
    print(hash(t))

