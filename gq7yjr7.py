colors = ["purple", "orange", "green"]

guess = input("なにいろでしょう？（入力してください）:")

if guess in colors:
    print("当たり")
else:
    print("ハズレ！また挑戦してね。")
