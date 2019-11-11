
# ----------------------------------------------------------------------------------
# Alt Solution 01
# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Python If-Else
# ----------------------------------------------------------------------------------
#
# Created: Nov 9, 2019
#
# Revision #N/A / Date: N/A
#
# Source:
# https://www.hackerrank.com/challenges/py-if-else/problem


# This solution does not follow the exact rules of the original, but it is an
# interesting implementation.


# ----------------------------------------------------------------------------------
# Original solution by Lari Liuhamo@Diapolo10
# ----------------------------------------------------------------------------------
def solution_01(n):
    # n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}
    print(f'{n:2} {check[n % 2 == 0 and (n in range(2, 6) or n > 20)]}')


print('\nOriginal implementation\n')
for x in range(1, 31):
    solution_01(x)


# ----------------------------------------------------------------------------------
# My implementation
# ----------------------------------------------------------------------------------
def solution_02(n):
    check = {True: 'Weird', False: 'Not Weird'}
    print(f'{n:2} {check[n % 2 != 0 or n in range(6, 21)]}')


print('\n\nMy implementation\n')
for x in range(1, 31):
    solution_02(x)
