print('hello'.upper())

fruit = list()
print(fruit)

fruit = ['apple','orange','pear']
print(fruit)
fruit.append('banana')
fruit.append('peach')
print(fruit)
print(fruit[0])
print(fruit[1])
fruit[0] = 'mango'
print(fruit)
fruit.pop()
print(fruit)
fruit.pop(0)
print(fruit)

print('banana' in fruit)
print('taiga' in fruit)

print(len(fruit))

menber = ('taiga','kouya','kazuma','kenzi')
print(menber)                                       #タプルはリストとほぼおなしだけど、中身の変更ができない、一つだけの場合最後にカンマをつける

color = {'apple':'red','banana':'yellow'}
print(color)
color['apple'] = 'tomato'
print(color)
color['taiga'] = 'black'
print(color)
print('taiga' in color)
print('black' in color)                               #辞書はキーをしていしないと取り出すとこができない

list = []
a = [3,5,6]
b = [5,6,1]
c = [6,0.6]
list.append(b)
list.append(a)
list.append(c)
print(list)
print(list[1][0])