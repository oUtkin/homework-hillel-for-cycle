# asking user to enter the number
# that number will be equal to number of rows
N = input('Please, enter the number of rows: ')

# checking that input is whole number
try:
    N = int(N)
except ValueError:
    print('Please, use only whole numbers')
    exit()


# 1) and 2) are simple cycles tha include only *
print('1)')
for i in range(1, N + 1):
    # Number of * is equal to number of rows minus value of i
    print('*' * (N + 1 - i))

print('2)')
for j in range(1, N + 1):
    # number of * is equal to value of j
    print('*' * j)

# 3) and 4) are cycles that have to include not only * but ' '
# number of rows is equal to quantity of symbol in one row
print('3)')
for k in range(1, N + 1):
    # sum of ' ' and * is equal to number of rows,
    # number of ' ' is equal to k minus 1
    # and number of * is equal to number of rows minus k
    print(' ' * (k - 1), '*' * (N + 1 - k), sep='')

print('4)')
for l in range(1, N + 1):
    # sum of ' ' and * is equal to number of rows,
    # number of ' ' is equal to number of rows minus l
    # and number of * is equal to value of l
    print(' ' * (N - l), '*' * l, sep='')
