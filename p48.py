import random
number = random.randint(1,20)
if number > 10:
    print('1,japan')
else:
    print('1,nippon')

import random
number = random.randint(1,30)
if number >= 10:
    print('2,a')
elif number <= 10 <= 25:
    print('2,b')
elif number > 25:
    print('2,c')

import random
age = random.randint(60,80)
ritire = age - 65
if ritire > 10:
    print('3,finish soon')
else:
    print('3,hard work')
