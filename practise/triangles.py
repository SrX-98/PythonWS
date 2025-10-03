s=int(input())
y=[]
for i in range(0,s):
    v=input().split()
    a=int(v[0])
    b=int(v[1])
    c=int(v[2])
    if (a+b)>c and (b+c)>a and (c+a)>b:
        d=1
        y.append(d)
    else:
        d=0
        y.append(d)
print(*y)