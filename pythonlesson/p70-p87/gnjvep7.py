songs = {"1": "fun",
        "2": "blue"
        "3": "me"
        "4": "floor"
        "5": "live"
        }

n = inpput("数字を入力してください:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません。")    