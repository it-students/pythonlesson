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


def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)


def f():
    z = 1 + 1

result = f()
print(result)


print(len("Monty"))

print(len("Python"))


age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")


def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")

ven_odd(2)
even_odd(3)