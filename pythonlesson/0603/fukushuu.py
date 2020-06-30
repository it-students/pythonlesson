list = [1,2,3,4,5]
tuple = (1,2,3,4,5)

for i in range(5):
    print(i)

for i in list:
    print(i)
for i,j in enumerate([1,2,3,4,5]):
    print(i,j)
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end ="")
    print()

moji = 'abcde'
print(moji[2])
print(moji[-1])
print(moji*2)

len(moji)
moji[::-1]
list.append(6)
list.pop(5)
import random
x = random.randint(1,6)
if x % 2 == 0:
    print(str(x)+'habuusuu')
else:
    print(str(x)+'hakisuu')
double = x * 2
y = random.randint(1,6)

add = x + y
multi = x * y
max = max(x,y)
lessthan = min(x,y)
type('1')
type(1)
type(1.1)
True
None
type(list)
type(tuple)
# Kome = teisuu  kome = hennsuu
# senntounisuuji _ ya - nado
a = 'a'
a = 'b'

2**3 2%3 2//3 2/3 2*3 2-3 2+3

score = random.rnadint(0,100)
if score <= 59:
    print('D')
elif 59 < score <= 69:
    print('C')
elif 69 < score <= 79:
    print('B')
elif 79 < score <= 89:
    print('A')
else:
    print('S')
