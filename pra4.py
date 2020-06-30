food = ['carry','chiken','fish']
food.append('meet')
pop = food.pop(0)
food[1] = 'apple'
print(food)

season = ('spring','summer','autum','winter')
print(season[3])
print(season[:3])
print(len(season))

color = {'apple':'red','banana':'yellow','peach':'pink'}
color ['orange'] = 'daidai'
del color ['banana']
color ['apple'] = 'blue'
print(color)

def odd(n):
    return n + 3
result = odd(8)
print(result)

def lessthan(a,b):
    if a < b:
        print(True)
    else:
        print(False)
lessthan(4,5)