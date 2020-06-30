i = 0 
while i < 10:
    print(i+1)
    i +=1

i = 10
while i > 0:
    print(i)
    i -=1

i = 10
while True:
    if i < 1:
        break
    print(i)
    i -=1

for i in range(10):
    print(i+1)

name = ['amuro','kinjou,','kakazu']
for i,v in enumerate (name):
    print(i+1,v)


for tate in range(9):
    for yoko in range(9):
        print((tate+1)* (yoko+1),end='')
    print()
