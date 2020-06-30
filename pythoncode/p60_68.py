#教科書P60~68まで
#h3ych4h
def f (x=2):
    return x ** x
print(f())#=>4
print(f(4))#=>256

#hm5svn9

def add_it(x,y=10):
    return x+y
result = add_it(2)#x=2
print(result)#=>2+10=12

#zhmxnqt
#グローバル変数
x = 1
y = 2
z = 3
#関数外で宣言しても関数内でも値の変更等ができる
def f():
    print(x)#=>1
    y = 50
    print(y)#=>50
#ローカル変数
def a():
    ax = 1
    ay = 2
    az = 3
    print(ax)
    print(ay)
    print(az)
ax = 2 #=>できない

#jcg5qwp

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a/b)
#bに０が入ると例外が起きる
#例外の際の処理
except ZeroDivisionError:
    print("b cannt be zero.")
#文字列を入れても例外が発生する
#対策
try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("Invalid input.")
#try内で定義された変数を使用すると例外が発生する
try:
    10/0
    c="I will never get defined."
except ZeroDivisionError:
    print(c)

#zhahdcg
#ドキュメンテーション文字列
def add(x,y):
    """
    Returns x + y.
    :param x:int.
    :param y:int.
    :return: int sum of x and y.
    """
    #関数の動作
    #関数の引数
    #引数の型
    #返り値
    return x + y