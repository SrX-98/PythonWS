s=input()
l=int(s)
a=0
total=[]    
for i in range(l):
    v=input().split()
    e=int(v[0])
    step=int(v[1])
    t=int(v[2])
    v1=[]
    for j in range(t):
            sum=e
            sum=sum+(step*j)
            v1.append(sum)
    for k in v1:
        a=a+k
    total.append(a)
    a=0
print(*total)