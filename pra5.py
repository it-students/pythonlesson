a = ['b']
print(a[-1])
print(a[0])

def add(a,b):
    return a + b

print(add(3,5))

def add_sub(a,b,c=7,d=8):
    return (a+b)- c-d
print(add_sub(40,10))

for i in range(10):
    print(i+1,end=' ')
print()

i = 0
while i < 10:
    print(i+1,end=' ')
    i+=1
