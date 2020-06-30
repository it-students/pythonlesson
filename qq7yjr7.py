colors = ["purple", "orange", "green"]

quess = input("何色でしょう？(入力してください）："）

if quess in colors:
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")