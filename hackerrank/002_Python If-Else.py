
'''
if n is odd => Weird
if n is even and in range 2 to 5 inclusive => Not Weird
if n is even and in range 6 to 20 inclusive => Weird
if n is even and n > 20 => Not Weird

INPUT: positive integer
CONSTRAINS: 1 <= n <= 100
'''


# All odd numbers are weird
def weird(n):

    if n < 1 or n > 100:
        # print('Invalid input!')
        pass
    elif not n % 2 == 0 or n in range(6, 21):
        print(f'{n:2} Weird')
    else:
        print(f'{n:2} Not Weird')


for x in range(31):
    # weird(x)
    pass

# print(12 in range(6, 21))
