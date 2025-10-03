numbers = input().split()
v = [int(num) for num in numbers]

m = v[0]
m1 = v[0]
for num in v:
    if num > m:
        m = num
    elif num < m1:
        m1 = num
print(str(m) + " " + str(m1))