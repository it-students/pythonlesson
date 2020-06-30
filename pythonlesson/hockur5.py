try:
    10/0
    c="I will neber get defined."
except ZeroDivisionError:
    print(c)