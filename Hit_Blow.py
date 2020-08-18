import random

ans = []
for _ in range(10):
    rand = random.randint(0, 9)
    if rand in ans:
        pass
    else:
        ans += [rand]
    if len(ans) == 4:
        break

while True:
    n = int(input("4桁の数字を入力してください?"))
    if n < 10000:
        hit = 0
        blow = 0
        n_list = [(n // pow(10, i) % 10) for i in range(4)]
        for i in range(4):
            if n_list[i] in ans:
                if n_list[i] == ans[i]:
                    hit += 1
                else:
                    blow += 1
        print("hit:{}, blow:{}".format(hit, blow))
        if hit == 4:
            print("正解です")
            break
    else:
        print("範囲外です")
