#h79ob7s
#for i in range(100):
    #print('Hello Word')

#z52c8z8
import math
#対角線の長さ
l = 4
w = 10
d = math.sqrt(1**2 + w**2)

#zcdx3yo
print("""これは、とても、とても、とても、
長い複数行のコードです""")

#hjcf2sa
print\
("""これは、とても、とても、とても、
長い複数行のコードです""")

#zdva5wq
x = 10
x +=1
print(x)

#jqw4m5r
x = 10
x -= 1
print(x)

#grdc195
print(13//5)

#zsqwukd
print(13%5)

#jerpe5u 
#偶数
print(12%2)

#gkudhcr
#奇数
print(11%2)

#hh9fqzy
print(14//3)

#zlkjjdp
print(14/3)

#h8vuwd4
print(2**3)

#ja9mech
print(1==1 or 1==2 or 1==3)

#htvy6g3
home = 'USA'
if home == 'USA':
    print('Hello USA')
else:
    print('Hello Word')

#jytyg5x
home = 'japan'
if home == 'USA':
    print('Hello USA')
else:
    print('Hello Word')

#z24ckye
x = 2
if x == 2:
    print('数値は２です')
if x % 2 == 0:
    print('数値は偶数です')
if x % 2 != 0:
    print('数値は奇数です')

#zrodgne
x = 10
y = 11
if x == 10:
    if y == 11:
        print(x+y)

#jpr265j
home = 'thailand'
if home == 'japan':
    print('Hello japan')
elif home == 'india':
    print('Hello india')
elif home == 'china':
    print('Hello china')
else:
    print('Hello World')

#hzyxgf4
x = 100
if x == 10:
    print('10!')
elif x == 20:
    print('20!')

if x == 100:
    print('xは100!')
if x % 2 == 0:
    print('xは偶数')
else:
    print('xは奇数')

#j9dctwl
def f(x):
    return x * 2
print(f(2))

#znqp8fk
def f(x):
    return x + 1
z = f(4)
if z == 5:
    print('z is 5')
else:
    print('z is not 5')

#gqmkft7.py
def f(x,y,z):
    return x + y * z

result = f(3,4,5)
print(result)

#j8qyqov
def f():
    z = 1 + 1
print(f())

#zynprpg
def even_odd():
    age = input('19')
    int_age = int(age)
    if int_age < 21:
        print('you are young')
    else:
        print('you are old')

#zzn22mz
def even_odd():
    n = 19
    if n % 2 == 0:
        print('n is even.')
    else:
        print('n is odd.')
print(even_odd())
print(even_odd())
print(even_odd())

#h3ych4h
def f(x=2):
    return x ** x
print(f())
print(f(4))

#hm5svn9
def add_it(x,y=10):
    return x + y
print(add_it(5))

#hgvnj4p
x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)
f()

#zclmda7
x = 100
def f():
    global x
    x += 1
    print(x)
f()

#zdllght
print('Hello'.upper())

#hfgpst5
print('Hello'.replace('o', '@'))

#h9w3z2m
fruit = ['Apple','Orange','Pear']
fruit.append('Banana')
fruit.append('Peach')
print(fruit)

#h4ahvf9
color = ['blue','green','yellow']
color[2] = 'red'
print(color)
item = color.pop()
print(color)

#hplqc4u
fruits = {'Apple':'Red','Banana':'yellow'}
fruits['Peach'] = 'pink'
print(fruits)
del fruits['Apple']
print(fruits)

#zqqc2jw
author = 'kafka'
print(author[0],author[1],author[2],author[3],author[4])

#zcpt9se
name = 'ウィリアム　フォークナー'
print('Hello {}'.format(name))

#he8u28
print('みずたまりをとびこえたんだぜ。３めーとるもあったんだ！'.split('。'))

#h2pjkso
first_three = 'abc'
result = '+'.join(first_three)
print(result)
result = ' '.join(first_three)
print(result)

#jfndhgx
s = '  the    '
s = s.strip()
print(s)

#hzc6asc
print('animal'.index('m'))

#zyrhaeg
print('line1\nline2\nline3')

#judcpx4
ivan = '死の代わりに一つの光があった'
print(ivan[:6])
print(ivan[6:])

#zeftpq8
shows  = ['got','narcos','vice']
for show in shows:
    print(show)

#j8wvp8c
tv = ['got','narcos','vice']
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

#zcvgklh
tv = ['got','narcos','vice']
coms = ['arrested','development','frinend','always','sunny']
all_shows = []
for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)
print(all_shows)

#j2gwlcy
x = 10
while x > 0:
    print('{}'.format(x),end=' ')
    x -= 1
print('Happy Newyear')

#qqjxjtq
for i in range(1,3):
    print(i,end=' ')
    for letter in ['a','b','c']:
        print(letter,end=' ')

#z7duawp
list1 = [1,2,3,4]
list2 = [5,6,7,8]
added =[]
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)