a = float(input())
b = float(input())
oper = input()
if oper == '+':
  print (a + b)
if oper == '-':
  print(a -b)
if oper == '*':
  print(a * b)
if oper == '/':
    if b!=0:
          print (a / b)
    else:
        print('Деление на 0!')
        
if oper == 'mod':
    if b!=0:
          print (a % b)
    else:
        print('Деление на 0!')
  
if oper =='pow':
    print (a**b)
if oper == 'div':
    if b!=0:
          print (a // b)
    else:
        print('Деление на 0!')

