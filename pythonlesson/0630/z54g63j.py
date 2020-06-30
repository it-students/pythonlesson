tv = ['got','narcos','vice']
i = 0
for i in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)