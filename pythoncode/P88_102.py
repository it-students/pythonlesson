#教科書P88~102まで
#文字列操作
#h59ygda

"""line one
   line two
   line three
"""
#三重クォートを使うと複数行書ける

#zqqc2jw

author - "Kafka"
author[0]#"K"
author[1]#"a"
author[2]#"f"
author[3]#"k"
author[4]#"a"

author[5]#error 範囲外

author[-1]#a 右から一番目の要素

author[-2]#k 右から二番目の要素
author[-3]#f 右から三番目の要素

#hsr831v

ff = "F.Fitzgerald"
ff = "F.Scott Fitzgerald"
ff
#=>F.Scott Fitzgerald

#h4z5mlg

#文字列の足し算

"cat"+"in"+"hat"
#=>catinhat
"cat "+"in "+"the "+"hat"
#=>cat in the hat

#文字列の掛け算

"cat"*3
#=>catcatcat

#大文字小文字変換

#hhancz6

#大文字変換　.upper()
"We hold these truths...".upper()
#=>WE HOLD THESE TRTHS...

#小文字変換　.lower()
"SO IT GOES.".lower()
#=>so it goes.

#文字列の最初を大文字　.capitalize()
"four score and...".capitalize()
#=>Four score and...

#書式化
#juvguy8

"こんちにわ、{}".format("ウィアリム・フォーナクー")
#=>こんちにわ、ウィアリム・フォーナクー

name = "坂本"
"こんにちわ、{}".format(name)
#=>こんにちわ、坂本

#{}は何個でも
author = "ウィリアム・フォークナー"
year_born = "1897"

"{}　は　{}　年に生まれました".format(author,year_born)
#=>ウィリアム・フォークナー　は　1897　年に生まれました

#gnrdsj9
what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうした：")

r = "{}は{}に{}で{}。".format(what,when,where,do)
print(r)

#分割
#he8u28o
#split(分割したい文字や記号)

"水たまりを飛び越えたんだ。３メートルもあったんだぜ！".split("。")
#=>["水たまりを飛び越えたんだ","３メートルもあったんだぜ！"]

#結合
#h2pjkso
#〇〇.joint(追加したい変数)

first_three = "abc"
result = "+".joint(first_three)
result
#=>a+b+c

words = ["The","fox","jumped","over","the","fence","."]
one = "".joint(words)#空白0
one
#=>Thefoxjumpedoverthefence.
#↓
words = ["The","fox","jumped","over","the","fence","."]
one = " ".joint(words)#空白1
one
#=>The fox jumped over the fence .

#空白除去
#jfndhgx

s = "   The   "
s = s.strip()
s
#=>The

#置換
#zha4uwo

equ = "All animals are equal."
equ = equ.replace("a","@")
print(equ)
#=>All @nim@ls @re equ@l. aを@に置き換えている

#文字捜索
#hzc6asc

"animals".index("m")
#=>3 4文字目にmがあるよ

"animals".index("z")
#=>errer 例外発生
#↓例外処理を追加
try:
    "animals".index("z")
except:
    print("Not found.")
#=>Not found

#包含
#hsnygwz

"Cat"in"Cat in the hat."
#=<True Catを含んでいますよ

"Bat"in"Cat in the hat."
#=>False Batを含んでいませんよ

#not in を使うと、包含していないかを見る
"Potter" not in "Harry"
#=>True Potterを含んでいませんよ

#エスケープ文字
#zj6hc4r

"彼女は"そうだね"といった"#error
#↓
"彼女は\"そうだね\"といった"#ok
#=>彼女は"そうだね"といった

#""で囲んでいたら''、''で囲んでいたら""
#でもエスケープできる

#改行
#zyrhaeg

print("line1\line2\line3")
#=>line1
#  line2
#  line3

#スライス
#h2rqj2a

fict = {"A","B","C","D"}
fict[0:3]
#=>{"A","B","C"}
#   [0] [1] [2]

#[開始位置:スライスする数]

ivan = "死の代わりにひとつの光があった"
ivan[0:6]
#=>死の代わりに
ivan[6:12]
#=>ひとつの光があった

#インデックス0から開始する際は省略可
ivan[:6]
#=>死の代わりに

#最後まで取りたいときは最後を省略可
ivan[6:]
#=>ひとつの光があった

#両方空だったらコピー
ivan[:]
#=>死の代わりにひとつの光があった