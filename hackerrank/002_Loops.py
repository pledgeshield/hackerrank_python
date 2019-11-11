
# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Loops
# ----------------------------------------------------------------------------------
#
# Created: Nov 11, 2019
#
# Revision #N/A / Date: N/A
#
# Source:
# https://www.hackerrank.com/challenges/python-loops/problem


'''
TASK:
Read an integer N. For all non-negative integers i < N, print i^2

INPUT: positive integer N

CONSTRAINS: 1 <= N <= 20

OUTPUT: Print N lines, one corresponding to each i.
'''


# ----------------------------------------------------------------------------------
# My implementation
# ----------------------------------------------------------------------------------

def env_01(n):
    if 20 < n < 1:
        print('Invalid input!')
    else:
        for x in range(n):
            print(x ** 2)


env_01(5)


# ----------------------------------------------------------------------------------
# Original solution by Tara DeVries @tarathedev
# ----------------------------------------------------------------------------------

def env_02(n):
    # This expression takes advantage of unpacking
    print(*[num ** 2 for num in range(n)], sep='\n')


env_02(5)
