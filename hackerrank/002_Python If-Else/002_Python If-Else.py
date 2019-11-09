
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


'''
Short description of the problem:

if n is odd => Weird
if n is even and in range 2 to  5 inclusive => Not Weird
if n is even and in range 6 to 20 inclusive => Weird
if n is even and n > 20 => Not Weird

INPUT: positive integer
CONSTRAINS: 1 <= n <= 100
'''


# All odd numbers are weird
def weird_or_not(n):
    '''
    Check if a number is Weird or Not Weird
    '''
    # Check for valid constrains
    if n < 1 or n > 100:
        # print('Invalid input!')
        pass
    elif not n % 2 == 0 or n in range(6, 21):
        print(f'{n:2} Weird')
    else:
        print(f'{n:2} Not Weird')


# Test input from 1 to 30
for x in range(31):
    weird_or_not(x)