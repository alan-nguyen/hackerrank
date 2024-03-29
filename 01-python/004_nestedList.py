"""
Given the names and grades for each student in a Physics class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
"""
if __name__ == '__main__':
    marksheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))