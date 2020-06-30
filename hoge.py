def double(n):
    return n * 2

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def add(a, b):
    return a + b

def max2(a, b):
    if (a >= b):
        return a
    return b
        

def max3(a, b, c):
    if (a >= b):
        if (a >= c):
            return a
        else: # a < b
            if (b >= c):
                return b
        return c

for row in range(9):
    for col in range(9):
        print((row + 1) * (col + 1), end = ' ')
    print()



create_row(1)
create_row(2)
for row in range(9):
    create_row(row + 1)
    print()
    
def create_row(row):
    for col in range(9):
        print(row * (col + 1 ), end=' ')
# max2(2, 4) => 4
# max3(3, 5, 4) => 5
# is_even(2) => True
# is_even(3) => False
# is_odd(2) => False
# is_odd(1) => True
# add(2,3) => 5