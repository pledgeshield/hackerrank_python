
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
    CONSTRAINS: 1 <= n <= 100
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
    # Check for valid constrains
    if n < 1 or n > 99:
        return f'Invalid input: {n}'
    elif not n % 2 == 0 or n in range(6, 21):
        return f'{n:2} Weird'
    else:
        return f'{n:2} Not Weird'


# Test input from -1 to 110
list(map(lambda x: print(weird_or_not(x)), range(-1, 110)))


# ----------------------------------------------------------------------------------
# Alternative solution by Lari Liuhamo@Diapolo10
# ----------------------------------------------------------------------------------

# This solution does not follow the exact rules of the original, but it is an
# interesting implementation.
def solution_01(n):
    # n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}
    print(f'{n:2} {check[n % 2 == 0 and (n in range(2, 6) or n > 20)]}')


print('\nOriginal implementation\n')
for x in range(1, 31):
    solution_01(x)


# ----------------------------------------------------------------------------------
# My alternative implementation based on Lari's solution
# ----------------------------------------------------------------------------------

def solution_02(n):
    check = {True: 'Weird', False: 'Not Weird'}
    print(f'{n:2} {check[n % 2 != 0 or n in range(6, 21)]}')


print('\n\nMy implementation\n')
for x in range(1, 31):
    solution_02(x)
