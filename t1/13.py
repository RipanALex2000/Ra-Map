n = int(input("n="))
v=[]
for i in range(n):
    x = int(input("v["+str(i)+"]="))
    v.append(x)
s=0
for i in range(n):
    s=s + v[i]
md=float(s/n)
print("suma e "+ str(s))
print("media e " +str(md))