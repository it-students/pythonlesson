"水たまりをとびこえたんだ。３メートルもあったんだぜ!".split("。")

first_three = "abc"
result "+".join(first_three)
result

words = ["The", "fox", "jumped", 
         "over", "the", "fence", "."]
one = "".join(words)
one

words = ["The", "fox", "jumped", 
         "over", "the", "fence", "."]
one = " ".join(words)
one

s = "   The    "
s = s.strip()
s

equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

"animals".index("m")
"animals".index("z")

try:
    "animals".index("z")
except:
    print("Not found.")

"Cat" in "Cat in the hat."

'彼女は\'そうだね\'と言った'

"彼女は'そうだね'と言った"

print("line1\nline2\nline3")

fict = ["トルストイ","カミュ","オーウェル",
        "ハクスリー","オースティン"]
fict[0:3]

ivan = "死の代わりに一つの光があった。"
ivan[0:6]
ivan[6:16]

ivan[:6]
ivan[6:]
ivan[:]

name = "Ted"
for character in name:
    print(character)

shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

coms = ("A. Dvelopment", "Friends", "Always Sunny")
for show in coms:
    print(show)

people = {"G.Bluth IT": "A. Development",
          "Braney": "HIMYM",
          "Dennis": "Always Sunny",
         } 

for character in people:
    print(character)

tv =["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Dvelopment", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
     all_shows.append(show)

print(all_shows)

for i in range(1,11):
    print(i)

x=10
while x>0:
    print('{}'.format(x))
    x-=1
print("Happy New Year!")

while True:
    print("Hello, World!")

for i in range(0,100):
    print(i)
    break

ps = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]

n = 0 
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n= (n+1)%3

for i in range(1,6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i+j)

print(added)

while input('y or n?') !='n':
    for i in range(1,6):
        print(i)
