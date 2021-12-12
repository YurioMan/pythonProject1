a = int (input ('a = '))
b = int (input ('b = '))
if b > 0:
    print('a : b = ', a/b)
else:
    print('Chislo ne sootvetstvuet')
    b = int (input ('Vvedite chislo b : '))
    if b == 0:
        print (' vi apple')
    else:
        print('a : b = ', a/b)
