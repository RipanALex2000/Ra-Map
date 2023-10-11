x = int(input("x="))
if x%2==0:
    print("Nu e prim")
else:
    i=3
    b=0
    while i<x/2:
        if x%i==0:
            b=1
        i+=2
    if b == 0:
        print("E prim")
    else:
        print("Nu e prim")
