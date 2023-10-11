n = int(input("n="))
v=[]
for i in range(n):
    x = int(input("v["+str(i)+"]="))
    v.append(x)
max=v[0]
min=v[0]
for i in range(n):
    if max < v[i]:
        max = v[i]
    if min > v[i]:
        min =v[i]
print("max = "+str(max)+" ,min = "+str(min))