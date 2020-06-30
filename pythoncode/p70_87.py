#教科書P70~87まで
#zdllght
#メソッド
"Hello".upper()#=>HELLO
"Hello".replace("o"," @")#=>Hell@

#h4go6kg

#リスト宣言
fruit = list()#[]でもいい
fruit#=>[]

fruit = ["Apple","Orange","Pear"]
fruit#=>["Apple","Orange","Pear"]

fruit.append("Banana")#最後に追加
fruit#=>["Apple","Orange","Pear","Banana"]

#リストは文字以外にも格納可能

fruit[0]#=>Apple
fruit[1]#=>Orange
#存在しないインデックス値で取り出そうとすると例外が発生
fruit[6]#=>error

#ミュータブル（変更可能）
fruit[1]="Peach"
fruit#=>["Apple","Peach","Pear",Banana]
#要素を取り除く
fruit#=>["Apple","Peach","Pear",Banana]
item = fruit.pop()#=>item ="Banana"
fruit#=>["Apple","Peach","Pear"]

#加算演算子で連結可能
colors = ["blue","green","yellow"]
fruit + colors#=>["Apple","Peach","Pear","blue","green","yellow"]

#特定の要素が含まれてるかを調べる
"Apple" in fruit#=>True
#特定の要素が含まれてないかを調べる
"Banana" not in fruit#=>True

#リストのサイズを調べる
len(fruit)#=>3

#gq7yjr7
#リストの中身を当てるプログラム
colors = ["purple","orange","green"]
guess = input("何色でしょうか？（入力してください）:")
if guess in colors:
    print("Exactly")
else:
    print("はずれ")

#zo88eal
#タプル
my_tuple = tuple()#()でも可
my_tuple #=>()

rndm = ("M.jackson",1958,True)
rndm#=>M.Fackson,1958,True

#タプルの要素が一つだけだったらカンマをつける
("self_taughet",)#タプル
(9)+1#タプルじゃない

#タプルは一度作成したら新しい要素を追加できない
rndm[0] = "star"#=>error
#取り出し方はリストと同じ
rndm[0]#=>M.jackson
#特定の要素が含まれているかを見る
1958 in rndm #=>True
#特定の要素が含まれていないかを見る
2020 not in rndm#=>True

#辞書
#zfn6hmw

my_dict = dict()#{}どっちか

fruit = {"Apple":"Red","Banana":"Yellow"}
fruit#=>{"Apple":"Red","Banana":"Yellow"}
#宣言後の追加
facts = dict()
#バリューを追加
facts["code"]="fun"
#キーで参照
facts["code"]#=>fun
facts["Bill"]="Gates"
facts["Bill"]#=>"Gates"
facts["founded"]=1776
facts["founded"]#=>1776

#キーが使われているかを見る
"Apple" in fruit#=>True
#キーが使われていないかを見る
"Orange" not in fruit#=>True

#gops9fz
#コンテナの中にコンテナを格納

lists = []

a = ["カニ","ウニ","イクラ"]
b = ["ワカメ","コンブ"]
c = ["アカミ","シロミ"]

lists.append(a)
lists.append(b)
lists.append(c)

print(lists)
#=>[["カニ","ウニ","イクラ"],["ワカメ","コンブ"],["アカミ","シロミ"]]

a = lists[0]
print(a)#=>["カニ","ウニ","イクラ"]
a.append("アワビ")
#新しい要素をaに追加したらlistsも更新される
print(a)#=>["カニ","ウニ","イクラ","アワビ"]
print(lists)
#=>[["カニ","ウニ","イクラ","アワビ"],["ワカメ","コンブ"],["アカミ","シロミ"]]

#リストの要素にタプル、タプルの要素にリスト、
#リスト、タプルの要素に辞書を持たせることができる

#z9dhema
#リスト
locations = []
#タプル
la = (34.0522,188.2437)
chicago = (41.8781,87.6298)

locations.append(la)
locations.append(chicago)

print(locations)
#=>[(34.0522,188.2437),(41.8781,87.6298)]

#ht7gpsd

#リスト
eights = ["Edgar Allan Poe","Charles Dickens"]
nines = ["Hemingway","Fitzgerald","Orwell"]
#タプル
authors = (eights,nines)
print(authors)
#=>(["Edgar Allan Poe","Charles Dickens"],["Hemingway","Fitzgerald","Orwell"])

#h8ck5er
#辞書
bday = {"Hemingway":"7.21.1899","Fitzgerald":"9.24.1896"}
#リスト
my_list =[bday] 
#=>[{"Hemingway":"7.21.1899","Fitzgerald":"9.24.1896"}]
#タプル
my_tuple = (bday,)
#=>({"Hemingway":"7.21.1899","Fitzgerald":"9.24.1896"})

#辞書のバリューとしてリスト、タプル、辞書を格納可能
#zqupwx4

ny = {
    #座標は初期設定から変えることないからタプル
    "座標":(40.7128,74.0059),
    #セレブは今後増えてくる可能性があるのでリストで後から追加可能にする
    "セレブ":[
        "ウッディ・アレン",
        "ジェイ・Z",
        "ケヴィン・ベーコン",
    ],
    #州と入れると対応した名前をだすために辞書
    "事実":{
        "州":"ニューヨーク",
        "国":"アメリカ",
    }
}