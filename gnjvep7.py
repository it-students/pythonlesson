songs = {'1': 'fun',
         '2': 'blue',
         '3': 'me',
         '4': 'floor',
         '5': 'line'
         }
n = input('数字を入力してください:')
if n in songs:
    song = song[n]
    print(song)
else:
    print('見つかりません。')
    