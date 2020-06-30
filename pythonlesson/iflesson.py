x = 5
y = 3
z = 6

if x > y:
    print('x is greater than y')
elif y > x:
    print('x is less than y')
else:
    print('x equals y')


if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
else:
    print(z)