def is_even(n):
    return n % 2 == 0
print(is_even(4))

def is_odd(n):
    return n % 2 == 1
print(is_odd(5))

def double(n):
    return n * 2
print(double(2))

def add(a,b):
    return a + b
print(add(1,2))

def multi(a,b):
    return a * b
print(multi(2,5))

def max(a,b):
    if a > b:
        return a
    else:
        return b
print(max(3,2))

def lessthan(a,b):
    return a < b
print(lessthan(1,2))

def gpa(score):
    if score <= 59:
        print('D')
    elif 60 <= score <= 69:
        print('C')
    elif 70 <= score <= 79:
        print('B')
    elif 80 <= score <= 89:
        print('A')
    else:
        print('S')
print(gpa(59))

def max_e3(a,b,c):
    if a > b:
        if a > c:
            return a
    if b > c:
        return b
    else:
        return c
print(max_e3(4,2,5))

for row in range(9):
    for col in range(9):
        print((row + 1) * (col + 1),end = ' ')
    print()