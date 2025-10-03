s=int(input())
a=[]
#have to add sort in ascending order here first
for i in range(0,s):
    v=input().split()
    a.append(v[i])
    for i in range(1,len(v)):
        if int(v[i-1])==int(v[i]):
              continue
        else:
            a.append(v[i])
print(*a)
