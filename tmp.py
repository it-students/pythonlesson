def double(n):
    return 2 * n

print(double(2))

def add(a,b):
    return  a + b
print(add(2,3))

def mymax(a,b):
    if a < b:
        print(b)
mymax(2,3)


def max2(a,b):
    if a > b:
        return a
    return b
print(max2(4,2))

def max3(a,b,c):
    if a >= b:
        if a >= c:
            return a
    else:
        if b >= c:
            return b
    return c
print(max3(2,5,3))

def create_low(n):
    create_low(1) = 1 2 3 4 5 6 7 8 9
    create_low(2) = 2 4 6 8 10 12 14 16 18
    create_low(3) = 3 6 9 12 15 18 21 24 27
    create_low(4) = 4 8 12 16 20 24 28 32 36
    create_low(5) = 5 10 15 20 25 30 35 40 45
    create_low(6) = 6 12 18 24 30 36 42 48 54
    create_low(7) = 7 14 21 28 35 42 49 56 63
    create_low(8) = 8 16 24 32 40 48 56 64 72
    create_low(9) = 9 18 27 36 45 54 63 72 81

for row in range(9):
    create_low(row + 1)
    print()
