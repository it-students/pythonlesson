def creat_row(row):
    for col in range(9):
        print(row * (col + 1), end=' ')
    print()

create_row(1)
create_row(2)

for row in range(9):
    create_row(row + 1)
    print()