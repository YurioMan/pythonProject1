a, b, c = int(input()), int(input()), int(input())
if (a >=b) and (a >=c):
    xmax = a
if (b >= a) and (b >= c):
    xmax = b
if (c >= a) and (c >= b):
    xmax = c
    
if (a <= b) and (a <= c):
    xmin = a
if (b <= a) and (b <= c):
    xmin = b
if (c <= a) and (c <= b):
    xmin = c
midl = a+b+c-xmax-xmin
 
print ( xmax,xmin,midl, sep='\n')
