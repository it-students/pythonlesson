qs = ['what is your name?',
      'What is your fav. color?',
      'What is your quest?']
n = 0
while True:
    print('Typre q to quit')
    a = input(qs[n])
    if a == 'q':
        break
    n = (n + 1) % 3