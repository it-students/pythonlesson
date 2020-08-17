from itertools import count
from random import randint


def checkfn(left, right, guess):
    if left <= right:
        ans = "l"
    else:
        ans = "h"
    return ans == guess


def display_card(title, left, right="*"):
    separator = "{0}{1}{0}".format("*" * 5, " " * 4)
    pattern = iter(f" {r} ") if right else iter("*" * 3)
    return "\n".join(
        [
            f" [{title}] ",
            separator,
            f"*   *    * {next(pattern)} *",
            f"* {l} *    * {next(pattern)} *",
            f"*   *    * {next(pattern)} *",
            separator,
        ]
    )


def create_title(title):
    separator = "*" * 14
    return "\n".join([separator, f"* {title} *", separator])


print(create_title("High & Low"))
for c in count(0):
    left, right = [randint(1, 13) for _ in range(2)]
    print(display_card("問題表示", left))
    guess = input("h(igh) or l(ow) :")
    print(display_card("結果表示", left, right))
    if not checkfn(right, left, guess):
        print("\tYou lose")
        break
    print("\tYou win")

print(f"{c} times you win")
