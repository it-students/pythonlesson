def f(x):
    return x * 2
print(f(5))

result = f(2)
print(result)

def f(x):
    return x * 2
z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")


def f():
    return 1 * 2
z = f()
print(z)

def f(x,y,z):
    return x + y + z

result = f(1,2,3)
print(result)

def f() :
    z = 1 + 1 

result = f()
print(result)

print(len('monkey'))

print(str(100))

print(int("1"))

print(float(100))

# int("prince") => もじをかずにしようとするとえらー

def even_odd(x):
    if x % 2 == 0:
        print('偶数')
    else:
        print('奇数')

even_odd(2)
even_odd(3)

def f(x=2):
    return x ** x
print(f())
print(f(4))

def add_it(x,y=10):
    return x + y

result = add_it(2,5)
print(result)

x = 1 
y = 2 
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()

x = 100

def f():
    global x 
    x += 1
    print(x)

f()