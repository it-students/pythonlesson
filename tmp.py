
"""
def bai(n):
    return 2 * n
print(bai(2))


def add(n,a):
    return n + a
print(add(2,3))


def mymax(n,a):
    if n > a:
        return n
    return a
print(mymax(2,3))


def max3(a,b,c):
    if (a > b):
        if (c > a):
            return c
        else:
            return a
    if (c > b):
        return c
    else:
        return b
print(max3(1,2,3))
#print(max3(1,3,2))
#print(max3(2,1,3))
#print(max3(2,3,1))
#print(max3(3,1,2))
#print(max3(3,2,1))


for row in range(9):
    for col in range(9):
        print(f'{row + 1} x {col + 1} = ', (row + 1) * (col + 1) ,end = ' ')

for row in range(9):
    for col in range(9):
        print((row + 1) * (col + 1) ,end = ' ')
    print()

def pp(n):
    for osero in range(9):
        print(n * (osero + 1), end = ' ')
#pp(1) => 1 2 3 4 ...
#pp(2) => 2 4 6 8 ...

for row in range(9):
    pp(row + 1)
    print()

"""

def f(seimei):
    sei, mei = seimei.split()
    return f'{mei} {sei}'

print(f('abeno seimei'))
