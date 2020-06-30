print('hello')
import random
x = random.randint(1,10)
y = random.randint(1,10)
z = random.randint(1,10)
if x >= y and x >= z :
    print('x')
    print(x)
elif y >= x and y >= z :
    print('y')
    print(y)
else :
    print('z')
    print(z)