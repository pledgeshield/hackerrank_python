# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Finding The Percentage
# ----------------------------------------------------------------------------------
# Created:  Nov 28, 2019
# Revision: N/A
# ----------------------------------------------------------------------------------
# Source:
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# ----------------------------------------------------------------------------------


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
Input:

3
Tom 67 68 69
Bob 70 98 63
Max 52 56 60
'''
