tv = ['got','narcos','vice']
i = 0
for i in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)