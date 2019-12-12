# ----------------------------------------------------------------------------------
# Name of The Problem:
# ----------------------------------------------------------------------------------
# Find the Runner-Up Score!
# ----------------------------------------------------------------------------------
# Created: Nov 12, 2019
# Revision: N/A
# ----------------------------------------------------------------------------------
# Source:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# My implementation
# ----------------------------------------------------------------------------------

def runner_up_score(n, lst):
    n = int(n)
    lst = [int(x) for x in lst.split(' ')]

    # Get rid of all max scores so the second high score would become max score
    print(max([x for x in lst if not x == max(lst)]))


runner_up_score('5', '2 3 6 6 5')
# => 5

runner_up_score('5', '2 5 6 6 3')
# => 5

runner_up_score('7', '5 2 7 3 8 3 4')
# => 7
