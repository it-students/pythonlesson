def double(n):
    return 2 * n
print(double(2))

def add(n,m):
    return n + m
print(add(2,3))

def mymax(a, b):
    if a < b:
        return b
    return a
print(mymax(2, 3))

def max3(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    else:
        if b <= c:
            return c
        else:
            return b
print(max3(2, 4, 3))

for row in range(9):
    for col in range(9):
        print((row + 1) * (col + 1) ,end = '  ')
    print()

def f(full_name):
    f_name, l_name = full_name.split()
    return f'{l_name} {f_name}'
print(f('Kanata Tengan'))

