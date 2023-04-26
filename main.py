N = int(input('Please, enter the number of rows: '))

print('1)')
for i in range(1, N + 1):
    print('*' * (N + 1 - i))

print('2)')
for j in range(1, N + 1):
    print('*' * j)

print('3)')
for k in range(1, N + 1):
    print(' ' * (k - 1), '*' * (N + 1 - k), sep='')

print('4)')
for l in range(1, N + 1):
    print(' ' * (N - l), '*' * l, sep='')
