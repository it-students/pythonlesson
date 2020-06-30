#教科書P50~59まで
#j9dctwl
def f(x):
    return x*2
print(f(2))#=>4

z = f(4)
if z == 5:
    print("z is 5")
else:
    print("z is not 5")

def a():
    return 1+1
print(a())#=>2

def sum(x,y,z):
    return x+y+z
print(sum(5,8,11))#=>24

def null():
    z = 1+1
print(null())#=>None

#zfkzqw6
len("Monty")#文字列の長さを取得　5

str(100)#string型に変換　"100"
int("1")#int型に変換　1
float(100)#float型に変換　100.0

int("100")#=>100
int(20.565)#=>20
float("20.684")#=>20.684
float(99)#=>99.0

int("Hello")#=>error

#zynprpg

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow,you are old!")
#=>Enter your age:〇〇

#zhy8y4m

def even_odd(x):
    if x %2 == 0:
        print("偶数！！")
    else:
        print("奇数”！！")
even_odd(2)#=>偶数！！
even_odd(3)#=>奇数！！
#関数を使うと行数を減らせる

#jk8lugl

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

#↓関数を使って短くする

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")
even_odd():
even_odd():
even_odd():
#上記二つは同じ動作をする