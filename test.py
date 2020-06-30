for i in range(100):
    print("Hello, World!")


print("こんにちは！")


x = 10
x += 1
x
print(x)


x = 10
x -= 1
print(x)


print(13 // 5)
print(13 % 5)
print(12 % 2)
print(11 % 2)
print(14 // 3)
print(14 / 3)
print(2 ** 3)
print(2 + 2 * 2)
print((2 + 2) * 2)
print(100 > 10)
print(100 < 10)
print(2 >= 2)
print(2 <= 2)
print( 2 == 2)
print(1 != 2)
print(2 != 1)
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 1)
print(1 == 1 and 10 != 2 and 2 < 10)
print(1 == 1 or 1 == 2)
print(1 == 2 or 2 == 1)
print(1 == 1 or 2 == 2)
print(1 == 1 or 1 == 2 or 1 == 3)
print(not 1 == 1)
print(not 1 == 2)


home = "アメリカ"
if home == "アメリカ":
    print("Hello, America!")
else:
    print("Hello, World!")


home = "日本"
if home == "アメリカ":
    print("Hello, America!")
else:
    print("Hello, World!")


home = "アメリカ"
if home == "アメリカ":
    print("Hello, America!")


x = 2
if x == 2:
    print("数値は２です。")
if x % 2 == 0:
    print("数値は偶数です。")
if x % 2 != 0:
    print("数値は奇数です。")


x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)


home = "タイ"
if home == "日本":
    print("Hello, Japan!")
elif home == "タイ":
    print("Hello, Thailand!")
elif home == "インド":
    print("Hello, India!")
elif home == "中国":
    print("Hello, China!")
else:
    print("Hello, World")


home = "火星"
if home == "日本":
    print("Hello, Japan!")
elif home == "タイ":
    print("Hello, Thailand!")
elif home == "インド":
    print("Hello, India!")
elif home == "中国":
    print("Hello, China!")
else:
    print("Hello, World")


x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("分かりません！")

if x == 100:
    print("xは偶数！")

if x % 2 == 0:
    print("xは偶数！")
else:
    print("xは奇数！")
