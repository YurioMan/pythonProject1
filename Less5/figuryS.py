xs = input ()

if xs == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    
if xs == "прямоугольник":
    a = float(input())
    b = float(input())
    S = a * b
    
if xs == "круг":
    r = float(input())
    i = 3.14
    S = i * r**2
print (S)
