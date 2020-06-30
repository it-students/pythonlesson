def create_row(row):
    for col in range(9):
        print(row * (col + 1),end=" ")


for row in range(9):
    create_row(row + 1)
    print()