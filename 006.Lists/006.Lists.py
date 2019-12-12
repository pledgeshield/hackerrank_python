
# ----------------------------------------------------------------------------------
# LISTS
# ----------------------------------------------------------------------------------


# NOTE: Discussions has some neat implementations, go check them

def solution_01():

    n = int(input())
    lst = []

    for i in range(n):
        line = input().split(' ')

        if line[0] == 'insert':
            lst.insert(int(line[1]), int(line[2]))
        elif line[0] == 'remove':
            lst.remove(int(line[1]))
        elif line[0] == 'append':
            lst.append(int(line[1]))
        elif line[0] == 'sort':
            lst.sort()
        elif line[0] == 'pop':
            lst.pop()
        elif line[0] == 'reverse':
            lst.sort(reverse=True)
        else:
            print(lst)


# solution_01()


def solution_02():

    n = int(input())
    lst = []

    def manipulate(data, lst_obj):
        instructions = {
            'insert': lambda: lst_obj.insert(int(data[1]), int(data[2])),
            'remove': lambda: lst_obj.remove(int(data[1])),
            'append': lambda: lst_obj.append(int(data[1])),
            'sort': lambda: lst_obj.sort(),
            'reverse': lambda: lst_obj.reverse(),
            'pop': lambda: lst_obj.pop(),
            'print': lambda: print(lst_obj)
        }

        if data[0] in instructions:
            instructions[data[0]]()

    for i in range(n):
        line = input().split(' ')
        manipulate(data=line, lst_obj=lst)


solution_02()


# Sample Input #1
'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

# Sample Input #2
'''
29
append 1
append 6
append 10
append 8
append 9
append 2
append 12
append 7
append 3
append 5
insert 8 66
insert 1 30
insert 6 75
insert 4 44
insert 9 67
insert 2 44
insert 9 21
insert 8 87
insert 1 75
insert 1 48
print
reverse
print
sort
print
append 2
append 5
remove 2
print
'''
