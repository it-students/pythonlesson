# 上に書いたコードを実行する方法はpythonlessonに移動した後、"Python3 [ファイル名]"で実行できる。
# dir ディレクトリ
# cat text.file | python3 first.py
# cat [参照するファイル名]　| python3 [ファイル名]

#第3章 プログラミング入門
for i in range(100):
    print("Hello,World!")
#これはコメントです
print("Hello,World")
#出力
print("python")
print("こんにちは！")
#行
print("""これは、とても、とても、とても、とても長い複数行のコードです。""")
print\
    ("""これは、とても、とても、とても、とても長い複数行のコードです。""")
#スペース
for i in range(100):
    print("Hello,World")
#データ型
print("Hello,World!")
print('Hello,World!')
print(2.2 + 2.2)
True
False
#定数と変数
print(2 + 2)
print(2 - 2)
print(4 / 2)
print(2 * 2)
b = 100
print(b)
x = 100
print(x)

x = 200
print(x)
x = 10
y = 10
z = x + y
print(z)
a = x - y
print(a) 
x = 10
x = x + 1
print(x)
x = 10
x = x - 1
print(x)
x = 10
x += 1
print(x)
x = 10
x -= 1
print(x)
#算術演算子
print(13 // 5)
print(13 % 5)
print(12 % 2)
print(14 // 3)
print(14 / 3)
print(2 ** 3)
print(2 + 2 * 2)
print((2 + 2) * 2)
#比較演算子
print(100 > 10)
print(100 < 10)
print(2 >= 2)
print(2 <= 2)
print(2 == 2)
print(1 == 2)
print(1 != 2)
print(2 != 2)
#論理演算子
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 2)
print(1 == 2 and 2 == 1)
print(2 == 1 and 1 == 1)
print(1 == 1 or 10 != 2 and 2 < 10)
print(1 == 1 or 1 == 2)
print(1 == 1 or 2 == 2)
print(1 == 2 or 2 == 1)
print(2 == 1 or 1 == 2)
print(1 == 1 or 1 == 2 or 1 == 3)
print(not 1 == 1)
#条件文
home = "アメリカ"
if home == "アメリカ":
    print("Hello,America!")
else:
    print("Hello,World")

home = "日本"
if home == "アメリカ":
    print("Hello,America!")
else:
    print("Hello,world!")

home = "アメリカ"
if home == "アメリカ":
    print("Hello,America")

x = 2 
if x == 2:
    print("数値は2です。")
if x % 2 == 0:
    print("数値は偶数です。")
if x % 2 != 0:
    print("数値は奇数です。")

x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)

home = "タイ"
if home =="日本":
    print("Hello,Japan!")
elif home == "タイ":
    print("Hello,Thailand!")
elif home == "インド":
    print("Hello,India!")
elif home == "中国":
    print("Hello,China!")
else:
    print("Hello,World")

home = "火星"
if home == "アメリカ":
    print("Hello,America!")
elif home == "カナダ":
    print("Hello,Canada!")
elif home == "タイ":
    print("Hello,Thailand!")
elif home == "メキシコ":
    print("Hllo,Mexico")
else:
    print("Hello,World")

x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("分かりません!")

if x == 100:
    print("xは100!")

if x % 2 == 0:
    print("xは偶数!")

#文
print("Hello,world!")
print(2 + 2)
for i in range(100):
    print("Hello,World!")
x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("わかりません！")

if x == 100:
    print("xは100!")

if x % 2 == 0:
    print("xは偶数!")
else:
    print("xは奇数!")
print("Michael")
print("Jordan")
#第4章 関数
def f(x):
    return x * 2
f (2)
result = f(2)
print(result)

def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

def f():
    return 1 + 1

result = f()
print(result)

def f(x,y,z) :
    return x + y + z
    
result = f(1,2,3)
print(result)

def f():
    z = 1 + 1

result = f ()
print(result)

len("Monday")
len("Python")
str(100)
int("1")
float(100)

int("100")
int(20.54)

float("16.4")
float(99)


age = input ("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow,you are old!")

def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else: print("奇数")

even_odd(2)
even_odd(3)

n = input("type a number:")
n = int(n)
if n % 2 == 0:
    print("n is even.")
else:
    print("n is odd.")

n = input("type a number:")
n = int(n)
if n % 2 == 0:
    print("n is even.")
else:
    print("n is odd.")

n = input("type a number:")
n = int(n)
if n % 2 == 0:
    print("n is even.")
else:
    print("n is odd.")

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()

def f(x=2):
    return x ** x

print(f())
print(f(4))


def add_it(x,y=10):
    return x + y

result = add_it(2)
print(result)

def add_it(x,y=10):
    return x + y

result = add_it(2)
print(result)

x = 1
y = 2 
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()

def f():
    x = 1
    y = 2 
    z = 3

print(x)
print(y)
print(z)

def f():
    x = 1
    y = 2 
    z = 3
print(x)
print(y)
print(z)

f()

if x > 100:
    print("x is > 100")

x = 100

def f():
    global x 
    x += 1
    print(x)

f()

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
print(a / b)

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
print(a / b)

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")