'''

print('Hello'.replace('o','@'))
print('Hello'.upper())
fruit = ['Apple','Orange','Pear']
fruit.append('Banana')
fruit.append('Peach')
print(fruit)

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append('Hello')
print(random)

fruit = ['Apple','Orange','Pear']
print(fruit[0])
print(fruit[1])
print(fruit[2])

colors = ['blue','green','yellow']
print(colors[2])
colors[2] = 'red'
print(colors)

colors = ['blue','green','yellow']
print(colors)
item = colors.pop()
print(item)
print(colors)
print('it\'s')
print()

W,H,x,y,r = map(int, input().split())
    if x - r <= 0:
        print('No')
    elif x + r < W:
        print('No')
    if x - r >= 0 and x + r <= W:
        print('Yes')
'''
'''
a,b,c = map(int,input().split())
d=0
for i in range(a,b+1):
    if c%i==0:
        d += 1
print(d)
'''
'''
x = 0
a,b,c = map(int,input().split())
for i in range(a,b+1):
    if c%i==0:
        x += 1
print(x)
'''

import string, itertools

for p in itertools.product(string.digits + string.ascii_lowercase, repeat=4):
    print(''.join(p))
    if ''.join(p) == '5135':
        print('ログイン成功')
        break
    else:
        print('ログイン失敗')