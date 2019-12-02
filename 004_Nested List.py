
# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Nested Lists
# ----------------------------------------------------------------------------------
# Created: Nov 24, 2019
# Revision #N/A / Date: N/A
# ----------------------------------------------------------------------------------
# Source:
# https://www.hackerrank.com/challenges/nested-list/problem
# ----------------------------------------------------------------------------------


'''
    TASK:

    Given the names and grades for each student in a Physics class of N students,
    store them in a nested list and print the name(s) of any student(s) having the
    second lowest grade.

    Note: If there are multiple students with the same grade, order their names
    alphabetically and print each name on a new line.


    INPUT:

    First line is an integer N, representing the number of students The 2N
    subsequent lines describe each student over two lines; the first line contains a
    student's name, and the second line contains their grade.

    CONSTRAINTS: 2 <= N <= 5 There will always be one or more students having the
    second lowest grade.


    OUTPUT:

    Print the name(s) of any student(s) having the second lowest grade in Physics;
    if there are multiple students, order their names alphabetically and print each
    one on a new line.
'''


# ----------------------------------------------------------------------------------
# My Solution #1
# ----------------------------------------------------------------------------------


def solution_01():

    student_list = []

    # Number of iterations are predefined by the input integer.
    # Asks for name and score during every iteration.
    for x in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])

    # Find the lowest grade
    lowest_gr = min(map(lambda x: x[1], student_list))

    # Create a new list which excludes all occurrences of lowest grade
    filtered_list = list(filter(lambda x: x[1] != lowest_gr, student_list))

    # Find second lowest grade
    second_gr = min(map(lambda x: x[1], filtered_list))

    # Store all students with second lowest grade in a new list
    result = list(filter(lambda x: x[1] == second_gr, filtered_list))

    # Sort the list by name
    result.sort(key=lambda x: x[0])

    # Output the names of the students with second lowest grade
    print('\nResult:')
    list(map(lambda item: print(item[0]), result))


solution_01()


# TODO: Write an algorithm which generates different lists(as below) for the above
# problem. Write an additional algorithm, who keeps statistics about successful
# attempt and errors, basically a log file.


# Possible inputs
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''

'''
2
Akriti
41
Harsh
39
'''

'''
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
'''
