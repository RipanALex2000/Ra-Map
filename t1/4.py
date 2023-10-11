x = int(input("x="))
y = int(input("y="))
while x != y:
    if x > y:
        x-=y
    else:
        y-=x
print(x)