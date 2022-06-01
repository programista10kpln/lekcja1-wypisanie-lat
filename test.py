from datetime import datetime

print('jesteś gotowy na wypisanie lat przestępnych naszej ery?')
while True:
    try:
        x = str(input('wpisz `tak` lub `nie`\n'))
        if x == 'tak':
            break
        elif x == 'nie':
            print('no to nie')
            exit()
        else:
            print('zla wartosc')
    except ValueError:
        print('zla wartosc')
        continue
x = 0
while x < datetime.now().year:
    x += 1
    if x % 4 == 0:
        print(x)
