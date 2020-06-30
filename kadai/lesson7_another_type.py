try:
    a = input("type a numbeer:")
    b = input("type a nother:")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError,ValueError):
    print("Invalid input")