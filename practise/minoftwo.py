s=input()
print(s)
m=[]
for i in range(0,int(s)):
    v=input().split()
    if int(v[0])>int(v[1]):
        m.append(int(v[1]))
    else:
        m.append(int(v[0]))
        
print(m)