A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print('Это нормально') 
else:
        if H < A:
            print('Недосып')
        else:
            if H > B:
                print ('Пересып')
