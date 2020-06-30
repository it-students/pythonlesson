def my_max(a,b):
    if a > b:
        return(a)
    return(b)

def max3(x,y,z):
    if my_max(x,y) < z:
        return(z)
    else:
        return(my_max(x,y))

#print(max3(12,17,14))

#for row in range(9):
    #for col in range(9):
        #print(f'{row + 1} x {col + 1} =',(row + 1) * (col + 1))
        #print((row + 1) * (col + 1),end= ' ')
    #print()


name = 'higashionna mao'

def name_1(name):
    l_name, f_name = name.split()
    return f_name, l_name

def name_2(name):
    x = name.index(' ')
    l_name = name[:x]
    f_name = name[x + 1:]
    return f_name, l_name

print(name_1(name))
print(name_2(name))