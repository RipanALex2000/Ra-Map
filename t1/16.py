import math as m
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
print(-b + m.sqrt(b*b-4*a*c))
x1 =-float((-b + m.sqrt(b*b-4*a*c))/2*a)
x2 = float((-b - m.sqrt(b*b-4*a*c))/2*a)

print("x1 ="+str(x1)+",x2= "+str(x2))