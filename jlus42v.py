try:
    a = input("type a number:")
    b = input("type a another:")
    a = input(a)
    a = input(b)
    print(a / b)
except(ZeroDivisionError):
    print("Invalid input.")