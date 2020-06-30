
#global section
x = 100

def f():
    global x        #local section
    x += 1
    print(x)

f()
