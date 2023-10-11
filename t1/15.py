n = int(input("n="))
v=[]
for i in range(n):
    x = int(input("v["+str(i)+"]="))
    v.append(x)
t = True 
while t:
    t = False
    for i in range(n-1):
        if v[i] > v[i+1]:
            t = True
            aux =  v[i]
            v[i] = v[i+1]
            v[i+1] = aux
for i in range(n):
    print(v[i])