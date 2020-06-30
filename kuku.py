def create_row(row):
for col in range(9):
    print(row * (col + 1),end=' ')

assert.equal(create_row(1),[1,2,3,4,5,6,7,8,9])
assert.equal(add(2,3),5)

create_row(1)
create_row(2)


for row in range(9):
    create_row(row + 1)
    print()


for row in range(9):
    for col in range(9):
        print((row + 1) * (col + 1),end = ' ')
    print()