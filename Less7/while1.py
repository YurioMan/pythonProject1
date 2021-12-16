'''n = int(input('Введите число: '))
c = 1
while c <= n:
    print ('*'* c)
    c += 1
'''

'''
n = int(input('Введите число: '))
star = '*'
while len(star) <= n:
    print(star)
    star += '*'
'''
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print ('**')
    if i > 2:
        print('***')
    i = i + 1

