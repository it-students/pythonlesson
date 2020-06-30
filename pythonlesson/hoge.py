def is_even(n):
    return 2 * n % 2 ==0
print(is_even(2))


def is_odd(n):
    return n % 2 == 1
print(is_odd(3))


def add(n,m):
    return n + m
print(add(4,8))


def multi(n,m):
    return n * m
print(multi(4,9))


def max(n,m):
    if n > m:
        return n
    return m
print(max(4,9))


def lessthan(n,m):
    if n < m:
        return n
    return m

print(lessthan(4,9))


def max3(a,b,c):
    if a < b:
        if b < c:
            return c
        else:
            return b
    else: # b < a
        if a < c:
            return c
        else:
            return a
    if c < a:
        if a < b:
            return b
        else:
            return a


print(max3(34,28,9))

def gpa(n):
    if n <= 59:
        return 'D'
    elif n <= 69:
        return 'C'
    elif n <= 79:
        return 'B'
    elif n <= 89:
        return 'A'
    else:
        return 'S'
print(gpa(87))

for row in range(9):
    for col in range(9):
        print((row + 1) * (col + 1), end = ' ')
    print()

def create_row(n):
    for row in range(9):

        print( n * (row + 1), end=' ')

create_row(3)

EOL = '0 0'
for e in iter(input,EOL):
    x, y = map(int, e.split())
    print('n'.join(list(map(str,sorted([x, y])))))


