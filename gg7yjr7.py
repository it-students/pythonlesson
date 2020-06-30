colors = ["purple", "orangee", "green"]


guess = input("何色でしょう？入力してください")

if guess in colors:
    print("あたり")
else:
    print("はずれ")