def gradingStudents(grades):
    # Write your code here
    return [grade + 5 - grade % 5 if grade >= 38 and grade % 5 >= 3
    else grade for grade in grades ]
