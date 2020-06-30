list = []
sport1 = ['soccer','baseball','tennis']
sport2 = ['volleyball','basketball',]
sport3 = ['kendo','judo','karate']

list.append(sport1)
list.append(sport2)
list.append(sport3)

print(list)
print (list[0])
#print(list[1])
list[0].append('ragubi-')
print(list[0])
list[0][3]='ameft'
print(list[0])
list1 = list[0].pop()
print(list[0])