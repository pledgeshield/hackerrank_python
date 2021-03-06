
# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Loops
# ----------------------------------------------------------------------------------
# Created:  Nov 11, 2019
# Revision: Dec 12, 2019
# ----------------------------------------------------------------------------------
# Source:
# https://www.hackerrank.com/challenges/python-loops/problem
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# My implementation
# ----------------------------------------------------------------------------------

def ver_01(n):
    if 20 < n < 1:
        print('Invalid input!')
    else:
        for x in range(n):
            print(x ** 2)


ver_01(5)


# Taking advantage of map():
def ver_02(n):
    list(map(print, [x ** 2 for x in range(n)]))


ver_02(5)


# ----------------------------------------------------------------------------------
# Original solution by Tara DeVries @tarathedev
# ----------------------------------------------------------------------------------

def env_01(n):
    # This expression takes advantage of unpacking:
    print(*[num ** 2 for num in range(n)], sep='\n')


env_01(5)
