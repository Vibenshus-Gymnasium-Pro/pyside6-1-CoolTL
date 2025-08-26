a = int(input())
b = int(input())
c = int(input())


d = b**2 - (4*a * c)

     

if d < 0:
    print ("Ingen løsning")
elif d == 0:
    x = -b/(2*a)
    print(x)
elif d > 0:
    x = (-b + d**0.5)/(2*a)
    y = (-b - d**0.5)/(2*a)
    if x <= y:
        print(x,  y)
    else:
        print(y, x)
    