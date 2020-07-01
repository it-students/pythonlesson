"Hello".upper()
"Hello".replace("o","@")

fruit = list()
fruit
fruit = []
fruit

fruit = ["Apple","Orange","Pear"]
fruit

fruit.append("Banana")
fruit.append("Peach")
fruit

fruit = ["Apple","Orange","Pear"]
fruit[0]
fruit[1]
fruit[2]

colors = ["blue","green","yellow"]
colors[4]
colors[2] = "red"
colors

colors = ["blue","green","yellow"]
item = colors.pop()
item
colors

colors1 = ["blue","green","yellow"]
colors2 = ["orange","pink","black"]
colors1 + colors2

colors = ["blue","green","yellow"]
"green" in colors
"black" in not colors

len(colors)

colors = ["purple","orange","green"]
guess = input("何色でしょう？（入力してください）:")

if guess in colors:
    print("あたり！")
else:
    print("ハズレ！また挑戦してね。")

my_tuple = ()
my_tuple

rndm = ("M.Jackson",1958, True)
rndm

(9) + 1

dys = ("1984","Brave New world","Fahrenheit 451")
dys[1] = "Handmaid's Tale"

dys = ("1984","Brave New world","Fahrenheit 451")
dys[2]

dys = ("1984","Brave New world","Fahrenheit 451")
"1984" in dys

dys = ("1984","Brave New world","Fahrenheit 451")
"Handmaid's Tale" not in dys

my_dict = dict()
my_dict

my_dict = {}
my_dict

fruit = {"Apple": "Red"
         "Banana": "Yellow"}
fruit

facts ["code"]
facts["Bill"] = "Gates"
facts["Bill"]
facts["founded"] = 1776
facts["founded"]

bill = {"Bill Gates": "charitable"}
"Bill Gates" in bill

books = {"Dracula": "Stoker",
      "1984": "Orwell",
         "The Trial": "Kafka"}

del books["The Trial"]
books

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"}

n = input("数字を入力してください:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません。")
lists = []
rap = ["カニエ・ウェスト","ジェイ・ｚ","エミネム","ナズ"]
rock = ["ボブ・ディラン","ザ・ビートルズ","レッド・ツェッペリン"]
djs = ["ゼッズ・デッド","ティエスト"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
rap = lists[0]
print(rap)

rap.append("ケンドリック・ラマー")
print(rap)
print(lists)

locations = []

la = (34.0522,188.2437)
chicago = (41.8781,87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["Edgar Allan Poe","Charles Dickens"]
nines = ["Hemingway","Fitzgarald","Orwell"]

authors = (eights,nines)
print(authors)

bday = {"hemingway": "7.21.1899",
            "Fitzgarald": "9.24.1896"}

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

ny = {"座標": (40.7128,74.0059),
      "セレブ": ["ウッディ・アレン",
                 "ジェイ・ｚ",
                 "ケヴィン・ベーコン",
                 ],
      "事実": {"州": "ニューヨーク",
               "国": "アメリカ",
               }
}

"""line one
   line two
   line three
"""

author = "Kafka"
author[0]
author[1]
author[2]
author[3]
author[4]

author[5]

author[-1]
author[-2]
author[-3]

ff="F.Fitzgerald"
ff="F.Scott Fitzgerald"
ff

"cat" + "in" + "hat"
"cat" + " in" + " the" + " hat"

"Sawyer"*3

"We hold three truths...".upper()
"SO IT GOES.".lower()
"four score and...".capitalize()

"こんにちは、{}".format("ウィリアム・フォークナー")
name = "ウィリアム・フォークナー"
"こんにちは、{}".format(name)

author = "ウィリアム・フォークナー"
year_born = "1897"

"{}は{}年に生まれました。".format(author,year_born)

what = input("何が:")
when = input("いつ:")
where = input("どこで":)
do = input("どうした":)

r = "{}は{}に{}で{}。".format(what,when,where,do)
print(r)
