# use Linear Function 
s=int(input())
a=[]
for i in range(s):
    v=input().split()
    x1=int(v[0])
    y1=int(v[1])
    x2=int(v[2])
    y2=int(v[3])
    m=int((y2-y1)/(x2-x1))# find the slope
    c=int(y1-(m*x1))# find the constant
    a.append((m,c))
print(' '.join(f'({m} {c})' for m, c in a))