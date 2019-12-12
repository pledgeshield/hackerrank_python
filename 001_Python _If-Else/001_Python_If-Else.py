
# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Python If-Else
# ----------------------------------------------------------------------------------
# Created: Nov 9, 2019
# Revision #N/A / Date: N/A
# ----------------------------------------------------------------------------------
# Source:
# https://www.hackerrank.com/challenges/py-if-else/problem
# ----------------------------------------------------------------------------------


'''
    Short description of the problem:

    if n is odd => Weird
    if n is even and in range 2 to  5 inclusive => Not Weird
    if n is even and in range 6 to 20 inclusive => Weird
    if n is even and n > 20 => Not Weird

    INPUT: positive integer
'''

# ----------------------------------------------------------------------------------
# My Solution #1
# ----------------------------------------------------------------------------------

# All odd numbers are weird
# All even numbers between 6 to 20 inclusive, are also weird


def weird_or_not(n):
    '''
    Check if a number is Weird or Not Weird
    '''
    if not n % 2 == 0 or n in range(6, 21):
        return f'{n:2} Weird'
    else:
        return f'{n:2} Not Weird'


# Test input from 1 to 31
list(map(lambda x: print(weird_or_not(x)), range(1, 31)))


# ----------------------------------------------------------------------------------
# Alternative solution by Lari Liuhamo@Diapolo10
# ----------------------------------------------------------------------------------

# This solution does not follow the exact rules of the original, but it is an
# interesting implementation.
def solution_01(n):
    # n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}
    return f'{n:2} {check[n % 2 == 0 and (n in range(2, 6) or n > 20)]}'


# Test input from 1 to 31
print('\nOriginal implementation:\n')
list(map(lambda x: print(solution_01(x)), range(1, 31)))


# ----------------------------------------------------------------------------------
# My alternative implementation based on Lari's solution
# ----------------------------------------------------------------------------------

def solution_02(n):
    check = {True: 'Weird', False: 'Not Weird'}
    return f'{n:2} {check[n % 2 != 0 or n in range(6, 21)]}'


# Test input from 1 to 31
print('\n\nMy implementation:\n')
list(map(lambda x: print(solution_02(x)), range(1, 31)))
