lines = list(map(str, range(1,11)))
with open("number.txt", "w") as f:
    f.write("\n".join(lines))

with open("number.txt", "r") as f:
    print(sum(map(int, list(f))))
#1～10のリスト
num = (list(map(str, range(1,11))))
print(num)

#何も返さない関数
def my_func(x):
    return x
print(my_func('take'))
add = lambda a, b: a + b

# リストの変更
def a(x, v):
    bef = [] + x
    bef.append(v)
    return bef
l = [0, 1, 2, 3]
print(l)
l2 = a(l, 1)
print(l2)
print(l)

#gcdを使わないで最大公約数を求める
def gre(a, b):
    a, b = max([a, b]),min([a, b])
    while b:
        a, b = b, a % b
    return a
print(gre(341,253))

#二進数への変換
def binary(n):
    buf = []
    while n:
        n, m = divmod(n, 2)
        buf.append(str(m))
    return "" .join(reversed(buf))
print(binary(16))

#フィボナッチ数列
def fib(n):
    buf = []
    a, b = 0, 1
    for _ in range(n-1):
        buf.append(a)
        a, b = b, a + b
    return buf
print(fib(10))

#成人　if else を使わないやり方
age = 21
message = 'adult' if (age >= 20) else 'chld'
print(message)

#普通にif elif を使ったやり方
def number_to_day(num=0):
    if num == 0:
        day = '今日'
    elif num == 1:
        day == '明日'
    elif num == -1:
        day == '昨日'
    else:
        day == '今日より1日を超えて離れた日'
    return day
print(number_to_day(0))

#日付　if elif else を使わないやり方
def f(num):
    return {
        '0': '今日',
        '1': '明日',
        '-1': '昨日'
    }.get(str(num), '今日より1日を超えて離れた日')
print(f(0),f(2))

#位置引数のタプル化
def concat_words(*args, separator='.'):
    return separator.join(args)
print(concat_words('a', 'b', 'c', 'd', separator='_'))

#変数に関数を代入
add = lambda a, b: a + b
print(add(1, 2))

s, t = 10, 3
print(["+" if i == t else "-" for i in range(s)])

print(dict([['a',1],['b',2]]))

#恋するハッカソン　おさげ
'''
n = int(input())
m = int(input())
tmp = 0
for i in range(m):
    tmp += int(input())
    if tmp > n*60:
        break

if i+1 == m:
    print("OK")
else:
    print(i)
'''
