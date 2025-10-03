#print("Enter two numbers:")
#a=int(input("Enter first number:"))
#b=int(input("Enter second number:"))
#d=a/b
#print(d)
#print(round(d))
m=[]
s=input()
l=int(s)
i=0
while i!=l:
    a=input().split()
    c=int(a[0])/int(a[1])
    r = int(c+0.5)#this rounds 0.5 to -0.5
    m.append(r)
    i+=1
print(*m)

from decimal import Decimal, ROUND_HALF_UP

m = []
s = input()
l = int(s)
for i in range(l):
    a = input().split()
    c = int(a[0]) / int(a[1])
    rounded = int(Decimal(str(c)).to_integral_value(rounding=ROUND_HALF_UP))
    m.append(rounded)
print(*m)
