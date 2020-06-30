i = 'abcdefg'
print(i)
print(i[0])
print(i[-1])
print(i[::-1])

print('iam,amuro,sho'.split(','))
j = i.replace('a','k')
print(j)
k = "+".join(j)
print(k)

print('animal'.index('i'))

print('amuro' in 'sho') 
print('u' in 'amuro')

print(i[:3])
print(i[3:])

name = ['amuro','kinjou','nakaza']
name.append('osiro')
name[0] = 'sueyosi'
name2 = name.pop()
print(name,name2)
print(name[:3])


sport = ('base','soccer','bask')
print(len(sport))
print(sport[1])

dict ={'apple':'red','banana':'yellow'}
dict  ['remon'] = 'yellow'
del dict  ['banana']
print(dict)

def is_even(x):
    if x % 2 ==0:
        print('even')
is_even(4)
    