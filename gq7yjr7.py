colors = ["purple", "orange", "green"]

guees = input("何色でしょう？(入力してください):")

if guees in colors:
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")