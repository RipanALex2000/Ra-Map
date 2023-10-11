a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a<b+c and b<a+c and c<a+b:
    print("Pot forma un triunghi")
else:
    print("NU pot forma un triunghi")