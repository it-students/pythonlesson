def double(n) :
    return 2 * n

#print(double(3))

def add(a,b) :
    return a + b

#print(add(2,3))

def max2(a,b) :
    if a > b :
        return a
    return b

#print(max2(2,3))

def max3(a,b,c) :
    if a >= b :
        if a >= c :
            return a
        else :
            return c
    else :
        if b > c :
            return b
        else :
            return c

#print(max3(5,7,9))

def max3(a,b,c) :
    return max2(max2(a,b) ,c)

#print(max(2,3,4,7,5))


def create_row(n) :
        for col in range(1,10) :
            print(n * col, end=" ")
        print()
#create_row(2)

s = ('Gackt syukumine').split(' ')

#print(s[1] + " " + s[0])

index = "Gakct syukumine".index(" ")
print(index)

name = "Gakct syujumine"
print(name[index + 1:])
print(name[:index])

print(name[index + 1:] + " " + name[:index])

i,j = 1,1
print(f'{i} + {j} = {i + j}')