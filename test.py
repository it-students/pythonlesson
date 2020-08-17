import random

# 0から9までのリスト作成
ans = [i for i in range(10)]

# リストをシャッフル
random.shuffle(ans)

# print(ans[:4])

while True:

    n = int(input('4桁の数字を入力してください?'))

    if n < 10000:

        hit = 0
        blow = 0

        # 桁ごとに分解
        n_list = [(n // pow(10, i) % 10) for i in range(4)]

        for i in range(4):

            if n_list[i] in ans[:4]:

                if n_list[i] == ans[i]:
                    hit += 1

                else:
                    blow += 1

        print('hit:{}, blow:{}'.format(hit, blow))

        if hit == 4:
            print('正解です')
            break

    else:
        print('範囲外です')
