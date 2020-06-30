def double(n):
    return 2 * n



def add (a, b):
    return a + b



def max2 (a, b):
    if a < b:
        return(b)
    return(a)



def max3 (a, b, c):
    return max2(max2(a, b), c)

#for row in range(9):
    #for col in range(9):
        #print((row + 1) * (col + 1) ,end =' ')
    #print()

def f(full_name):
    f_name, l_name = full_name.split()
    return f'{l_name} {f_name}'    
#print(f('seiya zayasu'))

def n(name):
    a = name.index(' ')
    return '{} {}'.format(name[a + 1:],name[:a + 1])
print(n('seiya zayasu'))