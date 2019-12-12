
# ----------------------------------------------------------------------------------
# Finding The Percentage
# ----------------------------------------------------------------------------------


'''
    record of N students consistitng of name and scores in three different
    subjects. Scores can be floats.

    INPUT:
        int - which designates the number of students
        every entry is: <name> <score> <score> <score>
        all the data need to be put in dictionary
        Maths, Physics and Chemistry

    OUTPUT:
        by imputing a student's name, output the avarage score, correct to two
        decimal places
'''


def env_01():

    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    print(f'{sum(student_marks[query_name]) / 3:.2f}')


env_01()


'''
3
Tom 67 68 69
Bob 70 98 63
Max 52 56 60
'''

# print(f'{56.0:.2f}')
