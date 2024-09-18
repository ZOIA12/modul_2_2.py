namber_1 = int(input('first: '))
namber_2 = int(input('second: '))
namber_3 = int(input('third: '))
if namber_1 == namber_2 and namber_2 == namber_3:
    print('3')
elif namber_1 == namber_2 or namber_2 == namber_3 or namber_1 == namber_3:
    print('2')
else:
    print('0')